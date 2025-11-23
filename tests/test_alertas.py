"""
Unit tests for the alert system (src/notificacoes/alertas.py)
Tests the evaluation of critical conditions and alert publishing logic
"""
import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch, MagicMock
from src.notificacoes.alertas import (
    avaliar_condicoes,
    publicar_alerta_sensor,
    limpar_historico_alertas,
    obter_status_throttling,
    ULTIMO_ALERTA
)


class TestAvaliarCondicoes:
    """Tests for avaliar_condicoes function"""
    
    def test_umidade_critica(self):
        """Test detection of critical humidity"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=55.0,
            ph=6.5,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 1
        assert "Umidade baixa" in condicoes[0]
        assert "55.0" in condicoes[0]
    
    def test_ph_baixo_critico(self):
        """Test detection of low pH"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=70.0,
            ph=5.5,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 1
        assert "pH fora da faixa" in condicoes[0]
        assert "5.50" in condicoes[0]
    
    def test_ph_alto_critico(self):
        """Test detection of high pH"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=70.0,
            ph=7.5,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 1
        assert "pH fora da faixa" in condicoes[0]
    
    def test_fosforo_critico(self):
        """Test detection of critical phosphorus"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=70.0,
            ph=6.5,
            fosforo_ok=False,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 1
        assert "Fósforo crítico" in condicoes[0]
    
    def test_potassio_critico(self):
        """Test detection of critical potassium"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=70.0,
            ph=6.5,
            fosforo_ok=True,
            potassio_ok=False,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 1
        assert "Potássio crítico" in condicoes[0]
    
    def test_irrigacao_ativa(self):
        """Test detection of active irrigation"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=70.0,
            ph=6.5,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=True
        )
        assert len(condicoes) == 1
        assert "Irrigação ativada" in condicoes[0]
    
    def test_multiplas_condicoes_criticas(self):
        """Test detection of multiple critical conditions"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=55.0,
            ph=5.5,
            fosforo_ok=False,
            potassio_ok=False,
            irrigacao_ativa=True
        )
        assert len(condicoes) == 5
    
    def test_nenhuma_condicao_critica(self):
        """Test when all conditions are normal"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=70.0,
            ph=6.5,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 0
    
    def test_valores_none(self):
        """Test handling of None values"""
        condicoes = avaliar_condicoes(
            sensor_id=1,
            umidade=None,
            ph=None,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        assert len(condicoes) == 0


class TestPublicarAlertaSensor:
    """Tests for publicar_alerta_sensor function"""
    
    def setup_method(self):
        """Clear alert history before each test"""
        limpar_historico_alertas()
    
    @patch('src.notificacoes.alertas.enviar_email')
    def test_alerta_enviado_com_sucesso(self, mock_enviar_email, mock_env_vars, monkeypatch):
        """Test successful alert sending"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        mock_enviar_email.return_value = {'MessageId': 'test-msg-id'}
        
        resultado = publicar_alerta_sensor(
            sensor_id=1,
            umidade=55.0,
            ph=5.5,
            fosforo_ok=False,
            potassio_ok=True,
            irrigacao_ativa=True
        )
        
        assert resultado is True
        assert mock_enviar_email.called
        
        # Verify alert was registered in history
        assert 1 in ULTIMO_ALERTA
    
    def test_sem_condicoes_criticas_nao_envia_alerta(self):
        """Test that no alert is sent when conditions are normal"""
        resultado = publicar_alerta_sensor(
            sensor_id=1,
            umidade=70.0,
            ph=6.5,
            fosforo_ok=True,
            potassio_ok=True,
            irrigacao_ativa=False
        )
        
        assert resultado is False
    
    @patch('src.notificacoes.alertas.enviar_email')
    def test_throttling_bloqueia_alertas_recentes(self, mock_enviar_email, mock_env_vars, monkeypatch):
        """Test that throttling blocks recent alerts"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        mock_enviar_email.return_value = {'MessageId': 'test-msg-id'}
        
        # First alert should succeed
        resultado1 = publicar_alerta_sensor(
            sensor_id=1,
            umidade=55.0,
            ph=5.5,
            fosforo_ok=False,
            potassio_ok=True,
            irrigacao_ativa=True
        )
        assert resultado1 is True
        
        # Second alert immediately after should be blocked
        resultado2 = publicar_alerta_sensor(
            sensor_id=1,
            umidade=50.0,
            ph=5.0,
            fosforo_ok=False,
            potassio_ok=False,
            irrigacao_ativa=True
        )
        assert resultado2 is False
        
        # Only one email should have been sent
        assert mock_enviar_email.call_count == 1
    
    @patch('src.notificacoes.alertas.enviar_email')
    def test_diferentes_sensores_podem_enviar_simultaneamente(self, mock_enviar_email, mock_env_vars, monkeypatch):
        """Test that different sensors can send alerts simultaneously"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        mock_enviar_email.return_value = {'MessageId': 'test-msg-id'}
        
        # Sensor 1
        resultado1 = publicar_alerta_sensor(sensor_id=1, umidade=55.0)
        assert resultado1 is True
        
        # Sensor 2 (different sensor)
        resultado2 = publicar_alerta_sensor(sensor_id=2, umidade=50.0)
        assert resultado2 is True
        
        # Both sensors should have sent alerts
        assert mock_enviar_email.call_count == 2
    
    @patch('src.notificacoes.alertas.enviar_email')
    def test_erro_no_envio_retorna_false(self, mock_enviar_email, mock_env_vars, monkeypatch):
        """Test that errors in sending return False"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        mock_enviar_email.side_effect = Exception("AWS SNS Error")
        
        resultado = publicar_alerta_sensor(
            sensor_id=1,
            umidade=55.0
        )
        
        assert resultado is False


class TestObterStatusThrottling:
    """Tests for obter_status_throttling function"""
    
    def setup_method(self):
        """Clear alert history before each test"""
        limpar_historico_alertas()
    
    def test_sem_alertas_anteriores(self):
        """Test status when no previous alerts exist"""
        status = obter_status_throttling(sensor_id=1)
        
        assert status['ultimo_alerta'] is None
        assert status['pode_enviar'] is True
        assert status['tempo_restante'] == 0
    
    @patch('src.notificacoes.alertas.enviar_email')
    def test_alerta_recente_nao_pode_enviar(self, mock_enviar_email, mock_env_vars, monkeypatch):
        """Test status immediately after sending alert"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        mock_enviar_email.return_value = {'MessageId': 'test-msg-id'}
        
        # Send alert
        publicar_alerta_sensor(sensor_id=1, umidade=55.0)
        
        # Check status
        status = obter_status_throttling(sensor_id=1)
        
        assert status['ultimo_alerta'] is not None
        assert status['pode_enviar'] is False
        assert status['tempo_restante'] > 0
    
    def test_alerta_antigo_pode_enviar(self):
        """Test status when enough time has passed"""
        # Manually set old alert time
        ULTIMO_ALERTA[1] = datetime.now(timezone.utc) - timedelta(minutes=20)
        
        status = obter_status_throttling(sensor_id=1)
        
        assert status['ultimo_alerta'] is not None
        assert status['pode_enviar'] is True
        assert status['tempo_restante'] == 0


class TestLimparHistoricoAlertas:
    """Tests for limpar_historico_alertas function"""
    
    def test_limpar_historico(self):
        """Test clearing alert history"""
        # Add some alerts to history
        ULTIMO_ALERTA[1] = datetime.now(timezone.utc)
        ULTIMO_ALERTA[2] = datetime.now(timezone.utc)
        
        assert len(ULTIMO_ALERTA) == 2
        
        limpar_historico_alertas()
        
        assert len(ULTIMO_ALERTA) == 0
