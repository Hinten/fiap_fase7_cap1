"""
AWS Rekognition Integration Package
====================================

Este pacote implementa a integração com o AWS Rekognition para análise
de imagens usando deep learning.

Módulos:
    rekognition_analyzer: Classe principal para análise de imagens
    aws_config: Gerenciamento de credenciais AWS
    example_usage: Exemplos de uso práticos
    setup_check: Verificação de instalação e configuração

Exemplo de uso:
    from rekognition_analyzer import RekognitionAnalyzer
    
    analyzer = RekognitionAnalyzer(region_name='us-east-1')
    response = analyzer.detect_labels(image_path='imagem.jpg')

Autor: FIAP - Fase 7 Cap 1
Data: 2025
"""

__version__ = '1.0.0'
__author__ = 'FIAP - Fase 7 Cap 1'

from .rekognition_analyzer import RekognitionAnalyzer
from .aws_config import (
    get_aws_credentials,
    print_credential_status,
    setup_aws_credentials_interactive
)

__all__ = [
    'RekognitionAnalyzer',
    'get_aws_credentials',
    'print_credential_status',
    'setup_aws_credentials_interactive'
]
