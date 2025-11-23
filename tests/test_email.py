"""
Unit tests for the email notification system (src/notificacoes/email.py)
Tests AWS SNS integration for sending emails
"""
import pytest
from unittest.mock import patch, MagicMock
from src.notificacoes.email import enviar_email, subscribe_email


class TestEnviarEmail:
    """Tests for enviar_email function"""
    
    @patch('src.notificacoes.email.boto3.client')
    @patch('src.notificacoes.email.SNS_TOPIC_ARN', 'arn:aws:sns:us-east-1:123456789012:test-topic')
    @patch('src.notificacoes.email.SNS_REGION', 'us-east-1')
    def test_enviar_email_com_sucesso(self, mock_boto3_client):
        """Test successful email sending"""
        # Setup mock
        mock_sns = MagicMock()
        mock_sns.publish.return_value = {
            'MessageId': 'test-message-id-12345',
            'SequenceNumber': '1'
        }
        mock_boto3_client.return_value = mock_sns
        
        # Execute
        assunto = "Teste de Email"
        mensagem = "Esta é uma mensagem de teste"
        resultado = enviar_email(assunto, mensagem)
        
        # Verify
        assert resultado is not None
        assert 'MessageId' in resultado
        assert resultado['MessageId'] == 'test-message-id-12345'
        
        # Verify SNS client was called
        mock_boto3_client.assert_called_once()
        mock_sns.publish.assert_called_once()
        
        # Verify publish parameters
        call_args = mock_sns.publish.call_args
        assert call_args[1]['Subject'] == assunto
        assert call_args[1]['Message'] == mensagem
    
    @patch('boto3.client')
    def test_enviar_email_com_assunto_longo(self, mock_boto3_client, mock_env_vars, monkeypatch):
        """Test sending email with long subject"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        # Setup mock
        mock_sns = MagicMock()
        mock_sns.publish.return_value = {'MessageId': 'test-id'}
        mock_boto3_client.return_value = mock_sns
        
        # Execute with long subject
        assunto = "A" * 200  # Very long subject
        mensagem = "Mensagem curta"
        resultado = enviar_email(assunto, mensagem)
        
        # Verify it was called (AWS will handle truncation if needed)
        assert resultado is not None
        mock_sns.publish.assert_called_once()
    
    @patch('boto3.client')
    def test_enviar_email_com_caracteres_especiais(self, mock_boto3_client, mock_env_vars, monkeypatch):
        """Test sending email with special characters"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        # Setup mock
        mock_sns = MagicMock()
        mock_sns.publish.return_value = {'MessageId': 'test-id'}
        mock_boto3_client.return_value = mock_sns
        
        # Execute with special characters
        assunto = "Alerta: Condições Críticas ⚠️"
        mensagem = "Umidade: 55.0% ⚠️\npH: 5.5 ⚠️\nFósforo: CRÍTICO ⚠️"
        resultado = enviar_email(assunto, mensagem)
        
        # Verify
        assert resultado is not None
        mock_sns.publish.assert_called_once()
    
    @patch('boto3.client')
    def test_enviar_email_falha_aws(self, mock_boto3_client, mock_env_vars, monkeypatch):
        """Test handling of AWS SNS failures"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        # Setup mock to raise exception
        mock_sns = MagicMock()
        mock_sns.publish.side_effect = Exception("AWS SNS Error")
        mock_boto3_client.return_value = mock_sns
        
        # Execute and expect exception
        with pytest.raises(Exception, match="AWS SNS Error"):
            enviar_email("Teste", "Mensagem")


class TestSubscribeEmail:
    """Tests for subscribe_email function"""
    
    @patch('src.notificacoes.email.boto3.client')
    @patch('src.notificacoes.email.SNS_TOPIC_ARN', 'arn:aws:sns:us-east-1:123456789012:test-topic')
    @patch('src.notificacoes.email.SNS_REGION', 'us-east-1')
    def test_subscribe_email_com_sucesso(self, mock_boto3_client):
        """Test successful email subscription"""
        # Setup mock
        mock_sns = MagicMock()
        mock_sns.subscribe.return_value = {
            'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:test-topic:sub-id'
        }
        mock_boto3_client.return_value = mock_sns
        
        # Execute
        email = "test@example.com"
        resultado = subscribe_email(email)
        
        # Verify
        assert resultado is not None
        assert 'SubscriptionArn' in resultado
        
        # Verify SNS client was called
        mock_boto3_client.assert_called_once()
        mock_sns.subscribe.assert_called_once()
        
        # Verify subscribe parameters
        call_args = mock_sns.subscribe.call_args
        assert call_args[1]['Protocol'] == 'email'
        assert call_args[1]['Endpoint'] == email
    
    @patch('boto3.client')
    def test_subscribe_email_invalido(self, mock_boto3_client, mock_env_vars, monkeypatch):
        """Test subscription with invalid email"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        # Setup mock to raise exception
        mock_sns = MagicMock()
        mock_sns.subscribe.side_effect = Exception("Invalid email format")
        mock_boto3_client.return_value = mock_sns
        
        # Execute and expect exception
        with pytest.raises(Exception, match="Invalid email format"):
            subscribe_email("invalid-email")
    
    @patch('boto3.client')
    def test_subscribe_multiplos_emails(self, mock_boto3_client, mock_env_vars, monkeypatch):
        """Test subscribing multiple emails"""
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        # Setup mock
        mock_sns = MagicMock()
        mock_sns.subscribe.return_value = {'SubscriptionArn': 'test-arn'}
        mock_boto3_client.return_value = mock_sns
        
        # Execute multiple subscriptions
        emails = ["test1@example.com", "test2@example.com", "test3@example.com"]
        for email in emails:
            resultado = subscribe_email(email)
            assert resultado is not None
        
        # Verify all were called
        assert mock_sns.subscribe.call_count == 3


class TestIntegrationEmailAlertas:
    """Integration tests for email and alert system"""
    
    @patch('boto3.client')
    def test_fluxo_completo_alerta_email(self, mock_boto3_client, mock_env_vars, monkeypatch):
        """Test complete flow from alert to email"""
        from src.notificacoes.alertas import publicar_alerta_sensor, limpar_historico_alertas
        
        # Setup environment
        for key, value in mock_env_vars.items():
            monkeypatch.setenv(key, value)
        
        # Clear history
        limpar_historico_alertas()
        
        # Setup mock
        mock_sns = MagicMock()
        mock_sns.publish.return_value = {'MessageId': 'test-msg-id'}
        mock_boto3_client.return_value = mock_sns
        
        # Execute alert
        resultado = publicar_alerta_sensor(
            sensor_id=1,
            umidade=55.0,
            ph=5.5,
            fosforo_ok=False
        )
        
        # Verify alert was sent
        assert resultado is True
        mock_sns.publish.assert_called_once()
        
        # Verify email content
        call_args = mock_sns.publish.call_args
        assert 'SENSOR 1' in call_args[1]['Subject']
        assert 'Umidade baixa' in call_args[1]['Message']
        assert 'pH fora da faixa' in call_args[1]['Message']
        assert 'Fósforo crítico' in call_args[1]['Message']
