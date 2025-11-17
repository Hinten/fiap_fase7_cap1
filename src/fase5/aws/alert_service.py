"""
AWS Alert Service - SNS/SES Integration
Serviço de alertas para o sistema FarmTech Solutions

Este módulo fornece integração com AWS SNS (Simple Notification Service)
para envio de alertas via email e SMS quando eventos críticos ocorrem.

Casos de uso:
- Fase 1: Condições climáticas adversas (geada, tempestade, seca)
- Fase 3: Sensores com valores críticos (umidade baixa, pH fora do ideal)
- Fase 6: Detecção de pragas ou doenças via YOLO

Autor: Grupo 28 - FIAP 2025
"""

import os
import logging
from typing import Optional, Dict, Any
from datetime import datetime

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
    BOTO3_AVAILABLE = True
except ImportError:
    BOTO3_AVAILABLE = False
    logging.warning("boto3 not installed. AWS alerts will be disabled.")


logger = logging.getLogger(__name__)


class AlertService:
    """
    Serviço de alertas AWS usando SNS (Simple Notification Service).
    
    Configuração necessária no .env:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
    - SNS_TOPIC_ARN
    
    Exemplos de uso:
    
    >>> from src.fase5.aws.alert_service import alert_service
    >>> 
    >>> # Alerta simples
    >>> alert_service.send_alert(
    ...     subject="Umidade Baixa",
    ...     message="Sensor detectou 25% de umidade"
    ... )
    >>> 
    >>> # Alerta com SMS adicional
    >>> alert_service.send_alert(
    ...     subject="Praga Detectada",
    ...     message="YOLO detectou lagarta no campo 3",
    ...     phone="+5511999999999"
    ... )
    """
    
    def __init__(self):
        """Inicializa o serviço de alertas AWS."""
        self._sns_client = None
        self._ses_client = None
        self._enabled = BOTO3_AVAILABLE
        
        if not self._enabled:
            logger.warning("AlertService initialized but boto3 is not available")
            return
        
        # Carregar configurações do ambiente
        self.aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.aws_region = os.getenv('AWS_REGION', 'us-east-1')
        self.sns_topic_arn = os.getenv('SNS_TOPIC_ARN')
        
        # Validar configurações essenciais
        if not all([self.aws_access_key, self.aws_secret_key, self.sns_topic_arn]):
            logger.warning(
                "AWS credentials or SNS topic ARN not configured. "
                "Alerts will be logged but not sent."
            )
            self._enabled = False
    
    @property
    def sns_client(self):
        """Lazy initialization do cliente SNS."""
        if self._sns_client is None and self._enabled:
            try:
                self._sns_client = boto3.client(
                    'sns',
                    aws_access_key_id=self.aws_access_key,
                    aws_secret_access_key=self.aws_secret_key,
                    region_name=self.aws_region
                )
            except Exception as e:
                logger.error(f"Failed to initialize SNS client: {e}")
                self._enabled = False
        return self._sns_client
    
    @property
    def ses_client(self):
        """Lazy initialization do cliente SES (opcional)."""
        if self._ses_client is None and self._enabled:
            try:
                self._ses_client = boto3.client(
                    'ses',
                    aws_access_key_id=self.aws_access_key,
                    aws_secret_access_key=self.aws_secret_key,
                    region_name=self.aws_region
                )
            except Exception as e:
                logger.error(f"Failed to initialize SES client: {e}")
        return self._ses_client
    
    def send_alert(
        self,
        subject: str,
        message: str,
        phone: Optional[str] = None,
        severity: str = "WARNING"
    ) -> Dict[str, Any]:
        """
        Envia um alerta via AWS SNS.
        
        Args:
            subject: Assunto do alerta (máx 100 caracteres)
            message: Corpo da mensagem do alerta
            phone: Número de telefone para SMS adicional (formato: +5511999999999)
            severity: Nível de severidade (INFO, WARNING, ERROR, CRITICAL)
        
        Returns:
            dict com status, message_id e timestamp
            
        Exemplos:
            >>> result = alert_service.send_alert(
            ...     subject="Temperatura Crítica",
            ...     message="Sensor DHT22-001 reportou 38°C",
            ...     severity="ERROR"
            ... )
            >>> print(result['status'])
            'success'
        """
        timestamp = datetime.now().isoformat()
        
        # Formatar mensagem com metadados
        formatted_message = self._format_message(message, severity, timestamp)
        
        # Truncar subject se necessário
        if len(subject) > 100:
            subject = subject[:97] + "..."
        
        # Log local sempre (backup)
        log_level = {
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }.get(severity, logging.WARNING)
        
        logger.log(log_level, f"ALERT: {subject} - {message}")
        
        # Se AWS não configurada, retornar apenas log
        if not self._enabled:
            return {
                "status": "logged_only",
                "message": "Alert logged but not sent (AWS not configured)",
                "timestamp": timestamp
            }
        
        try:
            # Enviar para tópico SNS (notifica todos os subscribers)
            response = self.sns_client.publish(
                TopicArn=self.sns_topic_arn,
                Subject=subject,
                Message=formatted_message,
                MessageAttributes={
                    'severity': {
                        'DataType': 'String',
                        'StringValue': severity
                    },
                    'timestamp': {
                        'DataType': 'String',
                        'StringValue': timestamp
                    }
                }
            )
            
            message_id = response.get('MessageId', 'unknown')
            logger.info(f"Alert sent successfully. MessageId: {message_id}")
            
            # Enviar SMS adicional se número fornecido
            if phone:
                self._send_sms(phone, f"{subject}\n\n{message}")
            
            return {
                "status": "success",
                "message_id": message_id,
                "timestamp": timestamp,
                "sms_sent": phone is not None
            }
            
        except NoCredentialsError:
            logger.error("AWS credentials not found or invalid")
            return {
                "status": "error",
                "error": "AWS credentials not configured",
                "timestamp": timestamp
            }
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            logger.error(f"AWS ClientError: {error_code} - {error_message}")
            return {
                "status": "error",
                "error": f"{error_code}: {error_message}",
                "timestamp": timestamp
            }
            
        except Exception as e:
            logger.error(f"Unexpected error sending alert: {e}")
            return {
                "status": "error",
                "error": str(e),
                "timestamp": timestamp
            }
    
    def _send_sms(self, phone: str, message: str) -> bool:
        """
        Envia SMS direto para um número específico.
        
        Nota: Requer verificação do número no sandbox AWS.
        """
        try:
            # Truncar mensagem se muito longa (SMS tem limite de ~160 caracteres)
            if len(message) > 160:
                message = message[:157] + "..."
            
            self.sns_client.publish(
                PhoneNumber=phone,
                Message=message
            )
            logger.info(f"SMS sent to {phone}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send SMS to {phone}: {e}")
            return False
    
    def _format_message(self, message: str, severity: str, timestamp: str) -> str:
        """Formata mensagem com cabeçalho padrão."""
        header = f"""
╔══════════════════════════════════════════════════════════╗
║  FarmTech Solutions - Sistema de Alertas                ║
║  Severidade: {severity:<43} ║
║  Data/Hora: {timestamp:<44} ║
╚══════════════════════════════════════════════════════════╝

{message}

---
Este é um alerta automático gerado pelo sistema FarmTech Solutions.
Para mais informações, acesse o dashboard ou contate o suporte.
"""
        return header.strip()
    
    def test_connection(self) -> Dict[str, Any]:
        """
        Testa a conexão com AWS SNS.
        
        Returns:
            dict com status do teste e informações do tópico
        """
        if not self._enabled:
            return {
                "status": "error",
                "message": "AWS not configured"
            }
        
        try:
            # Tentar obter atributos do tópico
            response = self.sns_client.get_topic_attributes(
                TopicArn=self.sns_topic_arn
            )
            
            attributes = response.get('Attributes', {})
            
            return {
                "status": "success",
                "topic_arn": self.sns_topic_arn,
                "topic_name": attributes.get('DisplayName', 'N/A'),
                "subscriptions_confirmed": attributes.get('SubscriptionsConfirmed', '0'),
                "subscriptions_pending": attributes.get('SubscriptionsPending', '0')
            }
            
        except Exception as e:
            logger.error(f"Connection test failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }


# Singleton instance
alert_service = AlertService()


# Helper functions para uso rápido
def publish_alert(
    subject: str,
    message: str,
    phone: Optional[str] = None,
    severity: str = "WARNING"
) -> Dict[str, Any]:
    """
    Helper function para envio rápido de alertas.
    
    Args:
        subject: Assunto do alerta
        message: Corpo da mensagem
        phone: Número de telefone para SMS (opcional)
        severity: Nível de severidade (INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        dict com resultado do envio
    
    Exemplo:
        >>> from src.fase5.aws.alert_service import publish_alert
        >>> publish_alert(
        ...     subject="Sensor Offline",
        ...     message="ESP32-001 não responde há 30 minutos",
        ...     severity="ERROR"
        ... )
    """
    return alert_service.send_alert(subject, message, phone, severity)


def test_aws_connection() -> Dict[str, Any]:
    """
    Testa a conexão com AWS SNS.
    
    Returns:
        dict com status do teste
    """
    return alert_service.test_connection()


if __name__ == "__main__":
    # Teste básico
    logging.basicConfig(level=logging.INFO)
    
    print("Testing AWS SNS connection...")
    result = test_aws_connection()
    print(f"Connection test: {result}")
    
    if result['status'] == 'success':
        print("\nSending test alert...")
        alert_result = publish_alert(
            subject="🧪 Teste do Sistema de Alertas",
            message="Este é um alerta de teste para validar o funcionamento do sistema AWS SNS.",
            severity="INFO"
        )
        print(f"Alert result: {alert_result}")
