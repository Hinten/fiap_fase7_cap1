"""
Módulo de Alertas de Sensores via AWS SNS

Este módulo é responsável por avaliar leituras de sensores e disparar alertas
automáticos via AWS SNS quando condições críticas são detectadas.

Funcionalidades:
- Avaliação de condições críticas (umidade, pH, nutrientes)
- Consolidação de múltiplas condições em um único alerta
- Throttling de 15 minutos entre alertas do mesmo sensor
- Armazenamento in-memory do controle de throttling
"""

from datetime import datetime, timedelta, timezone
from typing import Dict, List
from src.notificacoes.email import enviar_email

# Dicionário in-memory para controlar throttling de alertas
# Chave: sensor_id, Valor: datetime do último alerta enviado
# 
# LIMITAÇÃO: O armazenamento in-memory é perdido ao reiniciar a aplicação.
# Para ambientes de produção, considere usar:
# - Redis para cache distribuído
# - Tabela ALERTAS no banco de dados para persistência
# - Amazon ElastiCache para escalabilidade
ULTIMO_ALERTA: Dict[int, datetime] = {}

# Intervalo mínimo entre alertas (em minutos)
INTERVALO_MIN = 15


def avaliar_condicoes(sensor_id: int, umidade: float = None, ph: float = None, 
                      fosforo_ok: bool = True, potassio_ok: bool = True, 
                      irrigacao_ativa: bool = False) -> List[str]:
    """
    Avalia as condições dos sensores e retorna lista de condições críticas detectadas.
    
    Args:
        sensor_id: ID do sensor
        umidade: Valor da umidade (0-100%)
        ph: Valor do pH (0-14)
        fosforo_ok: Estado do sensor de fósforo (True = OK, False = Crítico)
        potassio_ok: Estado do sensor de potássio (True = OK, False = Crítico)
        irrigacao_ativa: Estado da irrigação (True = Ativa, False = Inativa)
    
    Returns:
        Lista de strings descrevendo as condições críticas encontradas
    """
    condicoes = []
    
    # Verifica umidade baixa
    if umidade is not None and umidade < 60:
        condicoes.append(f"Umidade baixa ({umidade:.1f}%) < 60%")
    
    # Verifica pH fora da faixa ideal
    if ph is not None and (ph < 6.0 or ph > 7.0):
        condicoes.append(f"pH fora da faixa ({ph:.2f}) - Ideal: 6.0–7.0")
    
    # Verifica fósforo crítico
    if not fosforo_ok:
        condicoes.append("Fósforo crítico")
    
    # Verifica potássio crítico
    if not potassio_ok:
        condicoes.append("Potássio crítico")
    
    # Verifica irrigação ativada
    if irrigacao_ativa:
        condicoes.append("Irrigação ativada")
    
    return condicoes


def publicar_alerta_sensor(sensor_id: int, umidade: float = None, ph: float = None,
                          fosforo_ok: bool = True, potassio_ok: bool = True,
                          irrigacao_ativa: bool = False) -> bool:
    """
    Avalia condições do sensor e publica alerta via SNS se necessário.
    
    Implementa throttling de 15 minutos: não envia alertas do mesmo sensor
    se já foi enviado um alerta nos últimos 15 minutos.
    
    Consolida múltiplas condições críticas em um único alerta.
    
    Args:
        sensor_id: ID do sensor
        umidade: Valor da umidade (0-100%)
        ph: Valor do pH (0-14)
        fosforo_ok: Estado do sensor de fósforo (True = OK, False = Crítico)
        potassio_ok: Estado do sensor de potássio (True = OK, False = Crítico)
        irrigacao_ativa: Estado da irrigação (True = Ativa, False = Inativa)
    
    Returns:
        True se alerta foi enviado, False caso contrário
    """
    # Avalia todas as condições
    condicoes = avaliar_condicoes(sensor_id, umidade, ph, fosforo_ok, potassio_ok, irrigacao_ativa)
    
    # Se não há condições críticas, não envia alerta
    if not condicoes:
        return False
    
    # Verifica throttling
    agora = datetime.now(timezone.utc)
    ultimo = ULTIMO_ALERTA.get(sensor_id)
    
    if ultimo and (agora - ultimo) < timedelta(minutes=INTERVALO_MIN):
        # Alerta recente já foi enviado, aguardar intervalo mínimo
        print(f"[THROTTLING] Alerta para sensor {sensor_id} bloqueado. "
              f"Último alerta: {ultimo.isoformat()}Z")
        return False
    
    # Monta o assunto do alerta
    assunto = f"[ALERTA SENSOR {sensor_id}] Condições Críticas Detectadas"
    
    # Monta a mensagem consolidada com todas as condições críticas
    mensagem = f"""ALERTA AUTOMÁTICO - SENSOR {sensor_id}

⚠️ CONDIÇÕES CRÍTICAS DETECTADAS ⚠️

Timestamp: {agora.isoformat()}Z

Condições críticas identificadas:
"""
    
    # Adiciona cada condição crítica
    for i, condicao in enumerate(condicoes, 1):
        mensagem += f"  {i}. {condicao}\n"
    
    # Adiciona valores atuais
    mensagem += f"""
Valores atuais:
  - Umidade: {f'{umidade:.1f}%' if umidade is not None else 'N/A'} {' ⚠️' if umidade is not None and umidade < 60 else ''}
  - pH: {f'{ph:.2f}' if ph is not None else 'N/A'} {' ⚠️' if ph is not None and (ph < 6.0 or ph > 7.0) else ''}
  - Fósforo: {'OK ✓' if fosforo_ok else 'CRÍTICO ⚠️'}
  - Potássio: {'OK ✓' if potassio_ok else 'CRÍTICO ⚠️'}
  - Irrigação: {'ATIVA ⚠️' if irrigacao_ativa else 'INATIVA'}

---
Este é um alerta automático gerado pelo sistema de monitoramento de sensores.
Próximo alerta poderá ser enviado após {INTERVALO_MIN} minutos.
"""
    
    try:
        # Envia o alerta via SNS
        resposta = enviar_email(assunto, mensagem)
        
        # Registra o horário do alerta
        ULTIMO_ALERTA[sensor_id] = agora
        
        print(f"[ALERTA ENVIADO] Sensor {sensor_id} - {len(condicoes)} condição(ões) crítica(s)")
        print(f"  MessageId: {resposta.get('MessageId', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"[ERRO] Falha ao enviar alerta para sensor {sensor_id}: {str(e)}")
        return False


def limpar_historico_alertas():
    """
    Limpa o histórico de alertas em memória.
    
    Útil para testes ou reinicialização do sistema.
    NOTA: Esta função não deve ser usada em produção pois remove o controle
    de throttling, podendo causar envio excessivo de alertas.
    """
    global ULTIMO_ALERTA
    ULTIMO_ALERTA.clear()
    print("[INFO] Histórico de alertas limpo")


def obter_status_throttling(sensor_id: int) -> Dict:
    """
    Retorna informações sobre o status de throttling de um sensor.
    
    Args:
        sensor_id: ID do sensor
    
    Returns:
        Dicionário com informações de throttling:
        - ultimo_alerta: datetime do último alerta (ou None)
        - pode_enviar: se pode enviar alerta agora
        - tempo_restante: segundos restantes até poder enviar (ou 0)
    """
    ultimo = ULTIMO_ALERTA.get(sensor_id)
    agora = datetime.now(timezone.utc)
    
    if not ultimo:
        return {
            'ultimo_alerta': None,
            'pode_enviar': True,
            'tempo_restante': 0
        }
    
    tempo_passado = agora - ultimo
    tempo_minimo = timedelta(minutes=INTERVALO_MIN)
    pode_enviar = tempo_passado >= tempo_minimo
    
    tempo_restante = 0 if pode_enviar else int((tempo_minimo - tempo_passado).total_seconds())
    
    return {
        'ultimo_alerta': ultimo,
        'pode_enviar': pode_enviar,
        'tempo_restante': tempo_restante
    }
