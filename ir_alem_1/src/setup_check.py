"""
Script de Setup e Verificação
==============================

Este script ajuda na configuração inicial do projeto e verifica se
tudo está instalado corretamente.

Executa as seguintes verificações:
1. Versão do Python
2. Dependências instaladas
3. Credenciais AWS configuradas
4. Acesso ao serviço Rekognition
5. Estrutura de diretórios

Autor: FIAP - Fase 7 Cap 1
Data: 2025
"""

import sys
import os
from pathlib import Path


def print_header(title):
    """Imprime um cabeçalho formatado"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def check_python_version():
    """Verifica se a versão do Python é compatível"""
    print_header("1. Verificando Versão do Python")
    
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✓ Versão do Python compatível (3.8+)")
        return True
    else:
        print("✗ Python 3.8 ou superior é necessário")
        print(f"  Versão atual: {version.major}.{version.minor}")
        return False


def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print_header("2. Verificando Dependências")
    
    required = {
        'boto3': 'AWS SDK',
        'botocore': 'AWS Core Library',
        'PIL': 'Pillow (Image Processing)',
        'requests': 'HTTP Library',
        'dotenv': 'Environment Variables'
    }
    
    all_installed = True
    
    for module, description in required.items():
        try:
            if module == 'PIL':
                __import__('PIL')
            elif module == 'dotenv':
                __import__('dotenv')
            else:
                __import__(module)
            print(f"✓ {description}")
        except ImportError:
            print(f"✗ {description} - NÃO INSTALADO")
            all_installed = False
    
    if not all_installed:
        print("\n⚠ Execute: pip install -r requirements.txt")
    
    return all_installed


def check_aws_credentials():
    """Verifica se as credenciais AWS estão configuradas"""
    print_header("3. Verificando Credenciais AWS")
    
    # Tenta carregar do módulo de configuração
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from aws_config import get_aws_credentials
        
        access_key, secret_key, region = get_aws_credentials()
        
        # Mascara credenciais
        masked_access = access_key[:4] + "*" * 8 + access_key[-4:]
        
        print(f"✓ Access Key ID: {masked_access}")
        print(f"✓ Region: {region}")
        
        # Verifica session token (necessário para Learner Lab)
        session_token = os.getenv('AWS_SESSION_TOKEN')
        if session_token:
            print(f"✓ Session Token configurado (Learner Lab)")
        else:
            print("⚠ Session Token não encontrado")
            print("  Se estiver usando Learner Lab, configure AWS_SESSION_TOKEN")
        
        return True
        
    except Exception as e:
        print(f"✗ Credenciais não configuradas: {str(e)}")
        print("\nConfigure usando uma das seguintes opções:")
        print("1. Arquivo .env na raiz do projeto")
        print("2. Variáveis de ambiente")
        print("3. Arquivo ~/.aws/credentials")
        return False


def check_rekognition_access():
    """Verifica se consegue acessar o Rekognition"""
    print_header("4. Verificando Acesso ao Rekognition")
    
    try:
        import boto3
        from botocore.exceptions import ClientError
        
        # Tenta criar cliente
        client = boto3.client('rekognition')
        
        # Não faz chamada real para não consumir créditos
        # Apenas verifica se o cliente foi criado
        print("✓ Cliente Rekognition criado com sucesso")
        print("✓ Credenciais parecem válidas")
        
        print("\n⚠ Nota: Não foi feita chamada real à API para economizar créditos")
        print("  Para testar completamente, execute os exemplos com uma imagem")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro ao criar cliente Rekognition: {str(e)}")
        return False


def check_directory_structure():
    """Verifica se a estrutura de diretórios está correta"""
    print_header("5. Verificando Estrutura de Diretórios")
    
    project_root = Path(__file__).parent.parent
    
    required_dirs = [
        'src',
        'examples',
        'docs',
        'docs/screenshots'
    ]
    
    all_exist = True
    
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"✓ {dir_path}/")
        else:
            print(f"✗ {dir_path}/ - NÃO ENCONTRADO")
            all_exist = False
    
    return all_exist


def create_missing_directories():
    """Cria diretórios faltantes"""
    print("\nCriando diretórios faltantes...")
    
    project_root = Path(__file__).parent.parent
    
    dirs_to_create = [
        'examples',
        'docs/screenshots'
    ]
    
    for dir_path in dirs_to_create:
        full_path = project_root / dir_path
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"✓ Criado: {dir_path}/")


def print_next_steps(results):
    """Imprime próximos passos baseado nos resultados"""
    print_header("Próximos Passos")
    
    if all(results.values()):
        print("🎉 Tudo configurado corretamente!")
        print("\nVocê pode:")
        print("1. Adicionar imagens de exemplo em examples/")
        print("2. Executar os exemplos: python src/example_usage.py")
        print("3. Testar análise: python src/rekognition_analyzer.py")
        print("4. Tirar screenshots do AWS Console para docs/screenshots/")
        
    else:
        print("⚠ Alguns problemas foram encontrados:\n")
        
        if not results['python']:
            print("❌ Atualize o Python para versão 3.8 ou superior")
        
        if not results['dependencies']:
            print("❌ Instale as dependências:")
            print("   pip install -r requirements.txt")
        
        if not results['credentials']:
            print("❌ Configure as credenciais AWS:")
            print("   1. Copie .env.example para .env")
            print("   2. Edite .env com suas credenciais")
            print("   3. Ou configure variáveis de ambiente")
        
        if not results['rekognition']:
            print("❌ Verifique suas credenciais AWS e permissões")
        
        if not results['directories']:
            print("❌ Execute novamente este script para criar diretórios")


def main():
    """Função principal"""
    print("\n" + "=" * 70)
    print("  AWS REKOGNITION - SETUP E VERIFICAÇÃO")
    print("  FIAP - Fase 7 Cap 1")
    print("=" * 70)
    
    # Executa todas as verificações
    results = {
        'python': check_python_version(),
        'dependencies': check_dependencies(),
        'credentials': check_aws_credentials(),
        'rekognition': False,  # Será verificado apenas se credenciais OK
        'directories': check_directory_structure()
    }
    
    # Verifica Rekognition apenas se dependências e credenciais OK
    if results['dependencies'] and results['credentials']:
        results['rekognition'] = check_rekognition_access()
    
    # Cria diretórios se necessário
    if not results['directories']:
        create_missing_directories()
        results['directories'] = True
    
    # Imprime resumo e próximos passos
    print_header("Resumo da Verificação")
    
    status_emoji = {True: "✓", False: "✗"}
    
    print(f"{status_emoji[results['python']]} Versão do Python")
    print(f"{status_emoji[results['dependencies']]} Dependências")
    print(f"{status_emoji[results['credentials']]} Credenciais AWS")
    print(f"{status_emoji[results['rekognition']]} Acesso ao Rekognition")
    print(f"{status_emoji[results['directories']]} Estrutura de Diretórios")
    
    print_next_steps(results)
    
    # Código de saída
    return 0 if all(results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
