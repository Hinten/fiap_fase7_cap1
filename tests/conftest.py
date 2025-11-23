"""
Pytest configuration and fixtures for FarmTech Solutions tests
"""
import pytest
import os
import sys
from unittest.mock import Mock, MagicMock

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def mock_env_vars():
    """Fixture to provide mock environment variables"""
    return {
        'SNS_REGION': 'us-east-1',
        'SNS_TOPIC_ARN': 'arn:aws:sns:us-east-1:123456789012:test-topic',
        'SQLITE': 'true',
        'LOGGING_ENABLED': 'true',
        'ENABLE_API': 'false'
    }


@pytest.fixture
def mock_boto3_client(monkeypatch):
    """Fixture to mock boto3 SNS client"""
    mock_client = MagicMock()
    mock_client.publish.return_value = {
        'MessageId': 'test-message-id-12345',
        'SequenceNumber': '1'
    }
    mock_client.subscribe.return_value = {
        'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:test-topic:sub-id'
    }
    
    def mock_boto3_client_func(service_name, region_name=None):
        return mock_client
    
    monkeypatch.setattr('boto3.client', mock_boto3_client_func)
    return mock_client


@pytest.fixture
def sample_sensor_data():
    """Fixture to provide sample sensor data"""
    return {
        'sensor_id': 1,
        'umidade': 55.0,
        'ph': 5.5,
        'fosforo_ok': False,
        'potassio_ok': True,
        'irrigacao_ativa': True
    }


@pytest.fixture
def sample_ml_input():
    """Fixture to provide sample ML model input"""
    from datetime import datetime
    return {
        'hora_leitura': datetime(2025, 5, 20, 14, 30, 0),
        'fosforo': 1,
        'potassio': 1,
        'ph': 1,
        'umidade': 45.5
    }
