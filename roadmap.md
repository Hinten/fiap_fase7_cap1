# 🗺️ Roadmap de Integração - Fase 7
## Consolidação das Fases 1-6 do Projeto FarmTech Solutions

Este documento descreve o plano detalhado de integração de todas as fases do projeto em um único sistema consolidado, incluindo a implementação do serviço de alertas AWS.

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Mapeamento dos Repositórios Originais](#mapeamento-dos-repositórios-originais)
3. [Etapas de Integração](#etapas-de-integração)
4. [Serviço de Alertas AWS](#serviço-de-alertas-aws)
5. [Cronograma](#cronograma)
6. [Riscos e Mitigações](#riscos-e-mitigações)

---

## 🎯 Visão Geral

### Objetivo

Unificar todas as funcionalidades desenvolvidas nas Fases 1-6 em um único projeto Python, com:
- Estrutura de pastas consolidada (`src/fase1/` até `src/fase7/`)
- Dashboard principal integrado (baseado na Fase 4)
- Sistema de alertas AWS (SNS/SES) recebendo eventos das Fases 1, 3 e 6
- Banco de dados centralizado (Fase 2) como backbone de dados
- Orquestração via CLI e dashboard

### Princípios de Design

1. **Mínima Modificação**: Preservar código funcional das fases anteriores
2. **Modularidade**: Cada fase permanece independente mas integrável
3. **Reutilização**: Aproveitar dashboards, APIs e modelos existentes
4. **Padronização**: Uniformizar imports, estrutura de pastas e configurações
5. **Escalabilidade**: Preparar para deploy em produção (AWS, Docker)

---

## 📦 Mapeamento dos Repositórios Originais

### Repositório Origem → Estrutura Consolidada

#### Fase 1: fiap_fase1_cap1-main

**Conteúdo Original:**
- `main.py` - Script principal com cálculos agrícolas
- `objetivo_a/` até `objetivo_h/` - Módulos por funcionalidade
- `culturas.json` - Base de dados de culturas
- `requirements.txt` - Dependências

**Destino na Consolidação:**
```
src/fase1/
├── __init__.py
├── agro_calculations.py     ← main.py adaptado
├── weather_api.py            ← integração API clima
├── culturas_loader.py        ← carrega culturas.json
└── utils/                    ← objetivos a-h modularizados
```

**Ações:**
- ✅ Copiar lógica de cálculo de área, insumos, etc.
- ✅ Extrair funções de API meteorológica
- ✅ Mover `culturas.json` para `data/culturas.json`
- ✅ Adaptar imports relativos para absolutos

---

#### Fase 2: fiap_fase2_cap1-master

**Conteúdo Original:**
- `assets/` - Diagramas MER/DER em PNG
- `README.md` - Documentação do modelo

**Destino na Consolidação:**
```
src/fase2/
├── __init__.py
├── models.py                 ← SQLAlchemy models (novo)
├── db.py                     ← engine, session, connection
├── migrations/               ← scripts SQL ou Alembic
│   └── initial_schema.sql
└── README.md                 ← mantido do original
```

**Ações:**
- ✅ Implementar models SQLAlchemy baseados no MER/DER
- ✅ Criar script de migração (DDL)
- ✅ Adicionar helper de conexão (Oracle + SQLite)
- ✅ Copiar assets (diagramas) para `docs/fase2/`

---

#### Fase 3: fiap_fase3_cap1-novo-main

**Conteúdo Original:**
- `main_dash.py` - Dashboard Streamlit existente
- `src/dashboard/` - Código do dashboard com CRUD
- `src/database/` - Models e lógica de DB
- `src/service/` - Integração API meteorológica
- `src/wokwi/` - Código ESP32 (sketch.ino)
- `requirements.txt`

**Destino na Consolidação:**
```
src/fase3/
├── __init__.py
├── api.py                    ← FastAPI endpoints (novo)
├── iot_handlers.py           ← lógica CRUD sensores
├── sensor_models.py          ← models de src/database/models/
├── esp32_examples/
│   ├── sketch.ino            ← código original ESP32
│   └── wokwi-project.txt
└── README.md
```

**Ações:**
- ✅ Extrair models de `src/database/models/` para `sensor_models.py`
- ✅ Criar API REST com FastAPI para receber dados do ESP32
- ✅ Migrar lógica de irrigação automática
- ✅ Copiar código ESP32 como referência
- ⚠️ **Dashboard será integrado na Fase 4**

---

#### Fase 4: fiap_fase4_cap1-main

**Conteúdo Original:**
- `main_dash.py` - Dashboard Streamlit + ML
- `src/dashboard/` - Views, plots, gráficos
- `src/modelo_preditivo/` - Notebooks e modelos treinados
- `src/wokwi_api/` - API para ESP32 + previsão
- `requirements.txt`

**Destino na Consolidação:**
```
src/fase4/
├── __init__.py
├── streamlit_app.py          ← DASHBOARD PRINCIPAL (integrado)
├── pages/                    ← páginas do dashboard por fase
│   ├── fase1_page.py
│   ├── fase2_page.py
│   ├── fase3_page.py
│   ├── fase5_page.py
│   └── fase6_page.py
├── ml/
│   ├── train.py              ← scripts de treinamento
│   ├── predict.py            ← inferência
│   └── models/               ← .pkl/.joblib salvos
└── components/               ← componentes reutilizáveis
```

**Ações:**
- ✅ **Refatorar `main_dash.py` como dashboard principal**
- ✅ Adicionar páginas/abas para cada fase
- ✅ Integrar plots e visualizações das Fases 3 e 4
- ✅ Adicionar botões de ação para disparar fases
- ✅ Migrar modelos ML para `ml/models/`
- ✅ Conectar com API da Fase 3

---

#### Fase 5: fiap_fase5_cap1-main

**Conteúdo Original:**
- `src/entrega_1/` - Notebooks ML (crop yield)
- `src/entrega_2/` - PDFs estimativa AWS
- `src/ir_alem_1/` - Sistema estufa ESP32
- `src/ir_alem_2/` - Monitoramento plantas
- `requirements.txt`

**Destino na Consolidação:**
```
src/fase5/
├── __init__.py
├── aws/
│   ├── __init__.py
│   ├── alert_service.py      ← SNS/SES integration (NOVO)
│   ├── iam_policy.md         ← políticas IAM necessárias
│   └── infra_notes.md        ← CloudFormation/Terraform
├── ml_models/                ← modelos da entrega_1
└── README.md
```

**Ações:**
- ✅ **IMPLEMENTAR serviço de alertas AWS** (SNS/SES)
- ✅ Criar `alert_service.py` com boto3
- ✅ Documentar setup AWS (tópico SNS, políticas IAM)
- ✅ Adicionar screenshots AWS no `docs/aws_screenshots/`
- ✅ Copiar notebooks ML como referência
- ✅ Documentar custos (usar PDFs da entrega_2)

---

#### Fase 6: fiap_fase6_cap1-main

**Conteúdo Original:**
- `src/entrega_1/` - Notebook YOLO padrão
- `src/entrega_2/` - YOLOv7 e CNN
- `src/ir_alem_1/` - Integração ESP32-CAM
- `src/ir_alem_2/` - Transfer learning, fine tuning
- Datasets no Google Drive

**Destino na Consolidação:**
```
src/fase6/
├── __init__.py
├── yolo_infer.py             ← wrapper YOLO inference (novo)
├── detection_service.py      ← API para detecção
├── models/
│   ├── best.pt               ← modelo treinado YOLO
│   └── cnn_model.h5          ← modelo CNN (backup)
├── camera/
│   └── esp32cam_sketch.ino   ← código ESP32-CAM
└── README.md
```

**Ações:**
- ✅ Implementar `yolo_infer.py` para inferência standalone
- ✅ Criar endpoint API para upload de imagens
- ✅ Integrar com sistema de alertas (se praga detectada)
- ✅ Copiar modelos treinados (best.pt)
- ✅ Adicionar código ESP32-CAM como exemplo

---

#### Fase 7: Consolidação (NOVO)

**Conteúdo:**
```
src/fase7/
├── __init__.py
├── orchestrator.py           ← lógica central de integração
├── launcher.py               ← CLI para disparar fases
└── config.py                 ← configurações centralizadas
```

**Funcionalidades:**
- CLI para executar fases individuais
- Orquestração de pipelines completos
- Logs centralizados de todas as operações
- Health checks de serviços

---

## 🔧 Etapas de Integração

### Etapa 1: Inventário e Preparação (✅ CONCLUÍDO)

**Atividades:**
- ✅ Clonar todos os repositórios originais
- ✅ Analisar estrutura de cada fase
- ✅ Listar dependências e conflitos
- ✅ Mapear pontos de integração
- ✅ Definir estrutura de pastas consolidada

**Entregáveis:**
- ✅ Este roadmap.md
- ✅ Estrutura `src/` criada
- ✅ Inventário de dependências

---

### Etapa 2: Criação da Estrutura Base (⏳ EM ANDAMENTO)

**Atividades:**
- ✅ Criar diretórios `src/fase1/` até `src/fase7/`
- ✅ Adicionar `__init__.py` em todos os módulos
- 🔄 Criar `requirements.txt` consolidado
- 🔄 Criar `.env.example` com todas as variáveis
- 🔄 Configurar `.gitignore` apropriado

**Comando:**
```bash
mkdir -p src/fase{1..7} src/fase5/aws docs/aws_screenshots tests
touch src/__init__.py src/fase{1..7}/__init__.py
```

**Entregáveis:**
- Estrutura de pastas completa
- Arquivo de configuração `.env.example`
- `.gitignore` atualizado

---

### Etapa 3: Implementação do Banco de Dados (Fase 2)

**Atividades:**
1. Criar models SQLAlchemy baseados no MER/DER
2. Implementar `db.py` com engine Oracle e SQLite
3. Escrever script de migração inicial
4. Testar conexões em ambos os bancos

**Código Exemplo (`src/fase2/models.py`):**
```python
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Propriedade(Base):
    __tablename__ = 'PROPRIEDADE'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(14))
    cidade = Column(String(255))

class Sensor(Base):
    __tablename__ = 'SENSOR'
    id = Column(Integer, primary_key=True)
    cod_serial = Column(String(255))
    tipo_sensor_id = Column(Integer, ForeignKey('TIPO_SENSOR.id'))
    plantio_id = Column(Integer, ForeignKey('PLANTIO.id'))
    nome = Column(String(255), nullable=False)
    # ... outros campos
```

**Testes:**
```bash
python -m src.fase2.db test_connection
python -m src.fase2.db migrate
```

---

### Etapa 4: Implementação de APIs (Fase 3)

**Atividades:**
1. Criar API REST com FastAPI
2. Endpoints para receber dados do ESP32
3. CRUD de sensores
4. Lógica de irrigação automática

**Código Exemplo (`src/fase3/api.py`):**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorReading(BaseModel):
    serial: str
    temperatura: float
    umidade: float
    ph: float

@app.post("/api/sensor/reading")
async def receive_reading(reading: SensorReading):
    # Salvar no banco (Fase 2)
    # Verificar thresholds
    # Se crítico, enviar alerta (Fase 5)
    return {"status": "ok"}
```

**Testes:**
```bash
uvicorn src.fase3.api:app --reload
curl -X POST http://localhost:8000/api/sensor/reading \
  -H "Content-Type: application/json" \
  -d '{"serial":"ESP32-001","temperatura":28.5,"umidade":62.3,"ph":6.8}'
```

---

### Etapa 5: Implementação do Serviço de Alertas AWS (Fase 5) ⚡ CRÍTICO

**Atividades:**
1. ✅ Criar conta AWS e configurar SNS
2. ✅ Implementar `alert_service.py` com boto3
3. ✅ Testar envio de email e SMS
4. ✅ Documentar setup com screenshots
5. ✅ Integrar com Fases 1, 3 e 6

**Setup AWS:**

```bash
# 1. Criar tópico SNS
aws sns create-topic --name farm-alerts --region us-east-1

# Saída esperada:
# {
#   "TopicArn": "arn:aws:sns:us-east-1:123456789:farm-alerts"
# }

# 2. Adicionar assinatura de email
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789:farm-alerts \
  --protocol email \
  --notification-endpoint contato@farmtech.com

# 3. Confirmar email (AWS envia link de confirmação)
```

**Código (`src/fase5/aws/alert_service.py`):**

```python
import os
import boto3
from typing import Optional

class AlertService:
    def __init__(self):
        self.sns_client = boto3.client(
            'sns',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION', 'us-east-1')
        )
        self.topic_arn = os.getenv('SNS_TOPIC_ARN')
    
    def send_alert(self, subject: str, message: str, 
                   phone: Optional[str] = None) -> dict:
        """
        Envia alerta via SNS (email) e opcionalmente SMS.
        
        Args:
            subject: Assunto do alerta
            message: Corpo da mensagem
            phone: Número de telefone para SMS (opcional)
        
        Returns:
            dict com MessageId e status
        """
        try:
            # Enviar para tópico SNS (email subscribers)
            response = self.sns_client.publish(
                TopicArn=self.topic_arn,
                Subject=subject,
                Message=message
            )
            
            # Opcionalmente enviar SMS direto
            if phone:
                self.sns_client.publish(
                    PhoneNumber=phone,
                    Message=f"{subject}\n\n{message}"
                )
            
            return {
                "status": "success",
                "message_id": response['MessageId']
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }

# Singleton
alert_service = AlertService()

def publish_alert(subject: str, message: str, phone: Optional[str] = None):
    """Helper function para uso rápido"""
    return alert_service.send_alert(subject, message, phone)
```

**Integração com Fase 3 (Sensor Crítico):**

```python
# src/fase3/api.py

from src.fase5.aws.alert_service import publish_alert

@app.post("/api/sensor/reading")
async def receive_reading(reading: SensorReading):
    # Salvar no banco
    save_to_db(reading)
    
    # Verificar thresholds
    if reading.umidade < 30:
        publish_alert(
            subject="⚠️ Alerta: Umidade Crítica",
            message=f"Sensor {reading.serial} reportou umidade de {reading.umidade}%"
        )
    
    return {"status": "ok"}
```

**Screenshots Necessários:**

Criar e salvar em `docs/aws_screenshots/`:
1. `sns_topic_created.png` - Tópico SNS criado no console
2. `sns_subscriptions.png` - Lista de assinantes (email/SMS)
3. `email_received.png` - Print do email de alerta recebido
4. `iam_policy.png` - Política IAM configurada

---

### Etapa 6: Integração de ML e YOLO (Fases 4 e 6)

**Atividades:**
1. Migrar modelos treinados para `src/fase4/ml/models/`
2. Implementar `yolo_infer.py` para detecção
3. Criar endpoint de upload de imagens
4. Integrar detecção → alerta AWS

**Código (`src/fase6/yolo_infer.py`):**

```python
from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self, model_path="src/fase6/models/best.pt"):
        self.model = YOLO(model_path)
    
    def detect(self, image_path: str, conf_threshold=0.5):
        """Detecta pragas/doenças em imagem"""
        results = self.model(image_path, conf=conf_threshold)
        
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class": result.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy.tolist()
                })
        
        return detections

# API endpoint
@app.post("/api/detect")
async def detect_pests(file: UploadFile):
    # Salvar imagem temporária
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    
    # Detectar
    detector = YOLODetector()
    detections = detector.detect(path)
    
    # Se praga detectada, alerta
    if any(d["class"] in ["praga", "doenca"] for d in detections):
        publish_alert(
            subject="🐛 Praga Detectada!",
            message=f"Detecções: {detections}"
        )
    
    return {"detections": detections}
```

---

### Etapa 7: Dashboard Unificado (Fase 4)

**Atividades:**
1. Refatorar `main_dash.py` da Fase 3/4
2. Adicionar menu lateral com todas as fases
3. Criar páginas para cada fase
4. Botões de ação para disparar serviços
5. Integrar visualizações

**Estrutura do Dashboard:**

```python
# src/fase4/streamlit_app.py

import streamlit as st

st.set_page_config(
    page_title="FarmTech Solutions - Dashboard Integrado",
    page_icon="🌾",
    layout="wide"
)

# Menu lateral
page = st.sidebar.selectbox(
    "Selecione a Fase",
    ["🏠 Home", "🌾 Fase 1", "💾 Fase 2", "🔌 Fase 3", 
     "📊 Fase 4", "☁️ Fase 5", "👁️ Fase 6", "🔧 Fase 7"]
)

if page == "🏠 Home":
    st.title("Sistema Agrícola Integrado - FarmTech Solutions")
    st.image("docs/architecture.png")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sensores Ativos", "12")
    with col2:
        st.metric("Alertas Hoje", "3")
    with col3:
        st.metric("Acurácia YOLO", "96%")

elif page == "🌾 Fase 1":
    from src.fase4.pages.fase1_page import render_fase1
    render_fase1()

elif page == "🔌 Fase 3":
    from src.fase4.pages.fase3_page import render_fase3
    render_fase3()
    
    # Botão de ação
    if st.button("▶️ Iniciar Monitoramento IoT"):
        st.info("Iniciando leitura de sensores...")
        # Chamar orquestrador
        from src.fase7.orchestrator import run_phase
        result = run_phase(3)
        st.success(f"Fase 3 executada: {result}")

# ... outras páginas
```

**Páginas Específicas (`src/fase4/pages/`):**

```python
# fase3_page.py - Monitoramento IoT

import streamlit as st
from src.fase2.db import SessionLocal
from src.fase2.models import Sensor, LeituraSensor

def render_fase3():
    st.header("🔌 Fase 3 - Monitoramento IoT")
    
    # Últimas leituras
    session = SessionLocal()
    leituras = session.query(LeituraSensor).order_by(
        LeituraSensor.data_leitura.desc()
    ).limit(50).all()
    
    df = pd.DataFrame([
        {
            "Sensor": l.sensor.nome,
            "Valor": l.valor,
            "Data": l.data_leitura
        }
        for l in leituras
    ])
    
    st.dataframe(df)
    
    # Gráfico de umidade
    st.line_chart(df[df["Sensor"].str.contains("Umidade")])
```

---

### Etapa 8: Orquestração (Fase 7)

**Atividades:**
1. Criar CLI launcher
2. Implementar `orchestrator.py`
3. Pipelines automatizados
4. Logs centralizados

**CLI (`src/fase7/launcher.py`):**

```python
import argparse
from src.fase7.orchestrator import run_phase

def main():
    parser = argparse.ArgumentParser(description="FarmTech Launcher")
    parser.add_argument("--fase", type=int, choices=range(1, 7),
                       help="Número da fase (1-6)")
    parser.add_argument("--all", action="store_true",
                       help="Executar todas as fases")
    
    args = parser.parse_args()
    
    if args.all:
        for fase in range(1, 7):
            print(f"\n🚀 Executando Fase {fase}...")
            run_phase(fase)
    elif args.fase:
        run_phase(args.fase)

if __name__ == "__main__":
    main()
```

**Orquestrador (`src/fase7/orchestrator.py`):**

```python
import logging

logger = logging.getLogger(__name__)

def run_phase(n: int) -> dict:
    """Executa lógica de uma fase específica"""
    
    logger.info(f"Iniciando Fase {n}")
    
    if n == 1:
        from src.fase1.agro_calculations import main as fase1_main
        return fase1_main()
    
    elif n == 3:
        from src.fase3.iot_handlers import start_monitoring
        return start_monitoring()
    
    elif n == 6:
        from src.fase6.yolo_infer import detect_and_store
        return detect_and_store()
    
    # ... outras fases
    
    else:
        raise ValueError(f"Fase {n} não implementada")
```

**Uso:**

```bash
# Executar fase individual
python -m src.fase7.launcher --fase 3

# Executar todas as fases em sequência
python -m src.fase7.launcher --all
```

---

### Etapa 9: Testes e Documentação

**Atividades:**
1. Escrever testes unitários para cada módulo
2. Testes de integração entre fases
3. Finalizar documentação
4. Screenshots AWS
5. Criar tutoriais de uso

**Estrutura de Testes:**

```
tests/
├── __init__.py
├── test_fase1_calculations.py
├── test_fase2_db.py
├── test_fase3_api.py
├── test_fase4_ml.py
├── test_fase5_aws_alerts.py
├── test_fase6_yolo.py
└── test_integration.py
```

**Exemplo de Teste:**

```python
# tests/test_fase5_aws_alerts.py

import pytest
from src.fase5.aws.alert_service import AlertService

def test_alert_service_send():
    service = AlertService()
    result = service.send_alert(
        subject="Teste",
        message="Alerta de teste"
    )
    assert result["status"] == "success"
    assert "message_id" in result
```

---

### Etapa 10: Deploy e Entrega Final

**Atividades:**
1. Revisar código completo
2. Garantir todos os testes passam
3. Finalizar README.md e roadmap.md
4. Adicionar screenshots AWS
5. Gravar vídeo demonstrativo
6. Fazer push final para GitHub

**Checklist Final:**

- ✅ README.md completo
- ✅ roadmap.md detalhado
- ✅ Estrutura `src/` consolidada
- ✅ Dashboard funcional
- ✅ Serviço de alertas AWS operacional
- ✅ Screenshots AWS incluídos
- ✅ requirements.txt atualizado
- ✅ .env.example criado
- ✅ Testes executando
- ✅ Documentação revisada

---

## 🚨 Serviço de Alertas AWS - Detalhamento

### Casos de Uso

#### 1. Alerta de Clima (Fase 1)

**Trigger:** API meteorológica detecta condição adversa

```python
# src/fase1/weather_api.py

def check_weather_alerts():
    weather = get_weather("Campinas,SP")
    
    if weather["temperatura"] < 5:
        publish_alert(
            subject="❄️ Alerta: Risco de Geada",
            message=f"Temperatura prevista: {weather['temperatura']}°C"
        )
    
    if weather["chuva_mm"] > 50:
        publish_alert(
            subject="🌧️ Alerta: Chuva Intensa",
            message=f"Precipitação prevista: {weather['chuva_mm']}mm"
        )
```

#### 2. Alerta de Sensor (Fase 3)

**Trigger:** Leitura de sensor fora do ideal

```python
# src/fase3/iot_handlers.py

def process_sensor_reading(reading):
    # Salvar no banco
    save_to_db(reading)
    
    # Verificar thresholds
    alerts = []
    
    if reading.umidade < 30:
        alerts.append("Umidade baixa (<30%)")
    
    if reading.ph < 5.5 or reading.ph > 7.5:
        alerts.append(f"pH fora do ideal ({reading.ph})")
    
    if alerts:
        publish_alert(
            subject=f"⚠️ Alerta: {reading.sensor_name}",
            message="\n".join(alerts)
        )
```

#### 3. Alerta de Visão (Fase 6)

**Trigger:** YOLO detecta praga ou doença

```python
# src/fase6/yolo_infer.py

def analyze_image(image_path):
    detections = yolo_model.detect(image_path)
    
    pests_found = [d for d in detections if d["class"] in ["praga", "lagarta"]]
    
    if pests_found:
        publish_alert(
            subject="🐛 Alerta: Praga Detectada",
            message=f"Detectado {len(pests_found)} pragas na imagem {image_path}"
        )
        
        # Salvar no banco para histórico
        save_detection(pests_found)
```

### Configuração AWS Passo a Passo

#### 1. Criar Tópico SNS

Via Console AWS:
1. Acessar SNS → Topics → Create topic
2. Type: Standard
3. Name: `farm-alerts`
4. Display name: `FarmTech Alerts`
5. Create topic

Via CLI:
```bash
aws sns create-topic --name farm-alerts --region us-east-1
```

#### 2. Criar Assinaturas

Email:
```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts \
  --protocol email \
  --notification-endpoint contato@farmtech.com
```

SMS:
```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts \
  --protocol sms \
  --notification-endpoint +5511999999999
```

#### 3. Configurar Política IAM

Criar usuário `farmtech-app` com política:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish",
        "sns:Subscribe",
        "sns:Unsubscribe",
        "sns:ListTopics",
        "sns:GetTopicAttributes"
      ],
      "Resource": "arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts"
    }
  ]
}
```

#### 4. Obter Credenciais

1. IAM → Users → farmtech-app → Security credentials
2. Create access key
3. Copiar Access Key ID e Secret Access Key
4. Adicionar no `.env`:

```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=abc123...
AWS_REGION=us-east-1
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts
```

#### 5. Testar

```python
from src.fase5.aws.alert_service import publish_alert

result = publish_alert(
    subject="Teste de Alerta",
    message="Se você recebeu este email, o sistema está funcionando!"
)
print(result)
```

---

## 📅 Cronograma

| Etapa | Descrição | Duração | Status |
|-------|-----------|---------|--------|
| 1 | Inventário e Preparação | 1 dia | ✅ CONCLUÍDO |
| 2 | Estrutura Base | 0.5 dia | ⏳ EM ANDAMENTO |
| 3 | Banco de Dados (Fase 2) | 1 dia | 🔜 PENDENTE |
| 4 | APIs IoT (Fase 3) | 1 dia | 🔜 PENDENTE |
| 5 | **Alertas AWS (Fase 5)** | **1.5 dias** | 🔜 PENDENTE |
| 6 | ML e YOLO (Fases 4 e 6) | 1.5 dias | 🔜 PENDENTE |
| 7 | Dashboard Unificado | 2 dias | 🔜 PENDENTE |
| 8 | Orquestração (Fase 7) | 1 dia | 🔜 PENDENTE |
| 9 | Testes e Documentação | 1.5 dias | 🔜 PENDENTE |
| 10 | Deploy e Entrega | 0.5 dia | 🔜 PENDENTE |
| **TOTAL** | | **11 dias** | **10% completo** |

---

## ⚠️ Riscos e Mitigações

### Risco 1: Conflitos de Dependências

**Descrição:** Fases usam versões diferentes de bibliotecas (ex: pandas 2.2.3 vs 2.1.0)

**Impacto:** ⚠️ MÉDIO

**Mitigação:**
- Criar `requirements.txt` consolidado com versões compatíveis
- Usar `pip freeze` após testes em ambiente limpo
- Priorizar versões mais recentes estáveis

### Risco 2: Credenciais AWS Inválidas

**Descrição:** Usuário não tem permissões SNS/SES corretas

**Impacto:** 🔴 ALTO (deliverable obrigatório)

**Mitigação:**
- Documentar políticas IAM exatas necessárias
- Fornecer script de teste de credenciais
- Criar usuário IAM dedicado com permissões mínimas

### Risco 3: Integrações Complexas

**Descrição:** Dashboard não consegue chamar APIs de outras fases

**Impacto:** ⚠️ MÉDIO

**Mitigação:**
- Usar imports absolutos (`from src.fase3.api import ...`)
- Testar módulos individualmente antes de integrar
- Criar `orchestrator.py` como camada de abstração

### Risco 4: Performance do Dashboard

**Descrição:** Dashboard lento com muitos dados/gráficos

**Impacto:** ⚠️ BAIXO

**Mitigação:**
- Usar cache do Streamlit (`@st.cache_data`)
- Limitar queries do banco (últimas 1000 leituras)
- Lazy loading de componentes pesados

### Risco 5: Custo AWS

**Descrição:** Testes excessivos geram cobrança

**Impacto:** 💰 BAIXO

**Mitigação:**
- SNS free tier: 1000 emails/mês, 100 SMS/mês
- Limitar testes a 10 alertas/dia
- Usar SNS sandbox mode (emails pré-verificados)

---

## 📚 Referências

### Documentação Oficial
- [AWS SNS](https://docs.aws.amazon.com/sns/)
- [Streamlit](https://docs.streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Ultralytics YOLO](https://docs.ultralytics.com/)

### Repositórios Originais
- [Fase 1](https://github.com/treino258/fiap_fase1_cap1)
- [Fase 2](https://github.com/treino258/fiap_fase2_cap1)
- [Fase 3](https://github.com/Hinten/fiap_fase3_cap1-novo)
- [Fase 4](https://github.com/Hinten/fiap_fase4_cap1)
- [Fase 5](https://github.com/Hinten/fiap_fase5_cap1)
- [Fase 6](https://github.com/Hinten/fiap_fase6_cap1)

---

## 🎯 Critérios de Aceitação

Para considerar a Fase 7 concluída, os seguintes critérios devem ser atendidos:

- ✅ README.md completo com instruções claras de instalação e execução
- ✅ roadmap.md detalhando todas as etapas de integração
- ✅ Estrutura `src/fase1/` até `src/fase7/` implementada
- ✅ Dashboard Streamlit integrado acessível via `streamlit run src/fase4/streamlit_app.py`
- ✅ Cada fase pode ser disparada via botão no dashboard ou CLI
- ✅ Serviço de alertas AWS (SNS) funcional com testes documentados
- ✅ Screenshots do console AWS mostrando tópico SNS e assinaturas
- ✅ Print de email/SMS recebido com alerta
- ✅ Banco de dados centralizado (Fase 2) integrando todas as fases
- ✅ API IoT (Fase 3) recebendo dados do ESP32 e salvando no DB
- ✅ YOLO (Fase 6) processando imagens e gerando alertas
- ✅ requirements.txt consolidado com todas as dependências
- ✅ .env.example com todas as variáveis necessárias
- ✅ Código testável (pelo menos testes básicos)

---

**Última Atualização:** 17/11/2025  
**Versão:** 1.0  
**Status:** ⏳ EM DESENVOLVIMENTO
