"""
Configuração de Credenciais AWS
================================

Este arquivo contém funções auxiliares para configurar as credenciais AWS
de forma segura, sem hardcode de chaves sensíveis no código.

IMPORTANTE: Nunca commite suas credenciais AWS no repositório!

Formas de configurar credenciais:
1. Variáveis de ambiente (recomendado)
2. Arquivo ~/.aws/credentials
3. Arquivo .env local (não commitado)
4. IAM Role (quando rodando em EC2/Lambda)

Autor: FIAP - Fase 7 Cap 1
Data: 2025
"""

import os
from pathlib import Path
from typing import Optional, Tuple
import configparser


def load_credentials_from_env() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Carrega credenciais AWS das variáveis de ambiente.
    
    Variáveis esperadas:
    - AWS_ACCESS_KEY_ID: Access Key ID
    - AWS_SECRET_ACCESS_KEY: Secret Access Key
    - AWS_DEFAULT_REGION: Região AWS (opcional, padrão: us-east-1)
    - AWS_SESSION_TOKEN: Token de sessão (opcional, necessário no Learner Lab)
    
    Returns:
        Tupla com (access_key, secret_key, region)
    """
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    session_token = os.getenv('AWS_SESSION_TOKEN')  # Necessário no Learner Lab
    
    return access_key, secret_key, region


def load_credentials_from_file(
    credentials_file: str = "~/.aws/credentials",
    profile: str = "default"
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Carrega credenciais do arquivo de credenciais AWS.
    
    O arquivo deve ter o formato:
    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY
    region = us-east-1
    
    Args:
        credentials_file: Caminho do arquivo de credenciais
        profile: Nome do perfil a usar
    
    Returns:
        Tupla com (access_key, secret_key, region)
    """
    credentials_path = Path(credentials_file).expanduser()
    
    if not credentials_path.exists():
        return None, None, None
    
    config = configparser.ConfigParser()
    config.read(credentials_path)
    
    if profile not in config:
        return None, None, None
    
    profile_config = config[profile]
    
    access_key = profile_config.get('aws_access_key_id')
    secret_key = profile_config.get('aws_secret_access_key')
    region = profile_config.get('region', 'us-east-1')
    
    return access_key, secret_key, region


def load_credentials_from_dotenv(dotenv_path: str = ".env") -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Carrega credenciais de um arquivo .env local.
    
    O arquivo .env deve conter:
    AWS_ACCESS_KEY_ID=your_access_key
    AWS_SECRET_ACCESS_KEY=your_secret_key
    AWS_DEFAULT_REGION=us-east-1
    AWS_SESSION_TOKEN=your_session_token  # Para Learner Lab
    
    Args:
        dotenv_path: Caminho do arquivo .env
    
    Returns:
        Tupla com (access_key, secret_key, region)
    """
    dotenv_file = Path(dotenv_path)
    
    if not dotenv_file.exists():
        return None, None, None
    
    # Lê o arquivo .env e define as variáveis de ambiente
    with open(dotenv_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
    
    return load_credentials_from_env()


def get_aws_credentials() -> Tuple[Optional[str], Optional[str], str]:
    """
    Obtém credenciais AWS tentando múltiplas fontes na seguinte ordem:
    1. Variáveis de ambiente
    2. Arquivo .env local
    3. Arquivo ~/.aws/credentials
    
    Returns:
        Tupla com (access_key, secret_key, region)
    
    Raises:
        ValueError: Se não for possível encontrar credenciais válidas
    """
    # Tenta variáveis de ambiente primeiro
    access_key, secret_key, region = load_credentials_from_env()
    if access_key and secret_key:
        return access_key, secret_key, region
    
    # Tenta arquivo .env
    access_key, secret_key, region = load_credentials_from_dotenv()
    if access_key and secret_key:
        return access_key, secret_key, region
    
    # Tenta arquivo de credenciais AWS
    access_key, secret_key, region = load_credentials_from_file()
    if access_key and secret_key:
        return access_key, secret_key, region
    
    # Nenhuma credencial encontrada
    raise ValueError(
        "Credenciais AWS não encontradas. Configure usando uma das seguintes opções:\n"
        "1. Variáveis de ambiente (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)\n"
        "2. Arquivo .env na raiz do projeto\n"
        "3. Arquivo ~/.aws/credentials"
    )


def print_credential_status():
    """
    Imprime o status das credenciais AWS configuradas.
    Útil para debugging sem expor as credenciais completas.
    """
    print("=" * 60)
    print("Status das Credenciais AWS")
    print("=" * 60)
    
    try:
        access_key, secret_key, region = get_aws_credentials()
        
        # Mascara as credenciais para segurança
        masked_access = access_key[:4] + "*" * (len(access_key) - 8) + access_key[-4:]
        masked_secret = secret_key[:4] + "*" * 12 + "****"
        
        print(f"\n✓ Credenciais encontradas:")
        print(f"  Access Key: {masked_access}")
        print(f"  Secret Key: {masked_secret}")
        print(f"  Region: {region}")
        
        # Verifica se há session token (necessário no Learner Lab)
        session_token = os.getenv('AWS_SESSION_TOKEN')
        if session_token:
            print(f"  Session Token: {session_token[:10]}...****")
            print("\n✓ Session token detectado (necessário para AWS Learner Lab)")
        else:
            print("\n⚠ Session token não encontrado")
            print("  Se estiver usando AWS Learner Lab, copie também o AWS_SESSION_TOKEN")
        
        print("\n✓ Configuração OK - Pronto para usar AWS Rekognition")
        
    except ValueError as e:
        print(f"\n❌ {str(e)}")
        print("\n" + "=" * 60)
        print("Como configurar no AWS Learner Lab:")
        print("=" * 60)
        print("\n1. Acesse o AWS Learner Lab")
        print("2. Clique em 'AWS Details'")
        print("3. Clique em 'Show' ao lado de 'AWS CLI'")
        print("4. Copie as três linhas (Access Key, Secret Key, Session Token)")
        print("5. Cole no terminal ou no arquivo .env")
        print("\nExemplo de arquivo .env:")
        print("-" * 60)
        print("AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE")
        print("AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
        print("AWS_SESSION_TOKEN=FwoGZXIvYXdzEPj//////////wEa...")
        print("AWS_DEFAULT_REGION=us-east-1")
        print("-" * 60)


def setup_aws_credentials_interactive():
    """
    Configuração interativa de credenciais AWS.
    Guia o usuário pelo processo de configuração.
    """
    print("\n" + "=" * 60)
    print("Configuração Interativa de Credenciais AWS")
    print("=" * 60)
    
    print("\nEste assistente irá ajudá-lo a configurar as credenciais AWS.")
    print("\nEscolha uma opção:")
    print("1. Configurar via variáveis de ambiente (temporário)")
    print("2. Criar arquivo .env (recomendado para desenvolvimento)")
    print("3. Configurar ~/.aws/credentials (persistente)")
    print("4. Verificar configuração atual")
    print("0. Sair")
    
    choice = input("\nOpção: ").strip()
    
    if choice == '1':
        print("\n" + "-" * 60)
        print("Configure as seguintes variáveis de ambiente:")
        print("-" * 60)
        print("\nexport AWS_ACCESS_KEY_ID='sua_access_key_id'")
        print("export AWS_SECRET_ACCESS_KEY='sua_secret_access_key'")
        print("export AWS_SESSION_TOKEN='seu_session_token'  # Se usar Learner Lab")
        print("export AWS_DEFAULT_REGION='us-east-1'")
        print("\nNo Windows (PowerShell):")
        print("$env:AWS_ACCESS_KEY_ID='sua_access_key_id'")
        print("$env:AWS_SECRET_ACCESS_KEY='sua_secret_access_key'")
        print("$env:AWS_SESSION_TOKEN='seu_session_token'")
        print("$env:AWS_DEFAULT_REGION='us-east-1'")
    
    elif choice == '2':
        print("\nCriando arquivo .env...")
        
        access_key = input("AWS Access Key ID: ").strip()
        secret_key = input("AWS Secret Access Key: ").strip()
        session_token = input("AWS Session Token (Enter para pular): ").strip()
        region = input("AWS Region [us-east-1]: ").strip() or 'us-east-1'
        
        env_content = f"""# Credenciais AWS - NÃO COMMITAR ESTE ARQUIVO!
# Este arquivo deve ser adicionado ao .gitignore

AWS_ACCESS_KEY_ID={access_key}
AWS_SECRET_ACCESS_KEY={secret_key}
AWS_DEFAULT_REGION={region}
"""
        
        if session_token:
            env_content += f"AWS_SESSION_TOKEN={session_token}\n"
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("\n✓ Arquivo .env criado com sucesso!")
        print("⚠ IMPORTANTE: Adicione '.env' ao seu .gitignore")
        
        # Verifica se .gitignore existe e adiciona .env se necessário
        gitignore_path = Path('.gitignore')
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                content = f.read()
            
            if '.env' not in content:
                with open(gitignore_path, 'a') as f:
                    f.write('\n# Credenciais AWS\n.env\n')
                print("✓ .env adicionado ao .gitignore")
        else:
            with open('.gitignore', 'w') as f:
                f.write('# Credenciais AWS\n.env\n')
            print("✓ .gitignore criado com .env")
    
    elif choice == '3':
        print("\nPara configurar ~/.aws/credentials:")
        print("1. Crie o diretório: mkdir -p ~/.aws")
        print("2. Edite o arquivo: nano ~/.aws/credentials")
        print("3. Adicione o seguinte conteúdo:")
        print("\n[default]")
        print("aws_access_key_id = SUA_ACCESS_KEY")
        print("aws_secret_access_key = SUA_SECRET_KEY")
        print("region = us-east-1")
        print("\n4. Salve e feche o arquivo")
    
    elif choice == '4':
        print_credential_status()
    
    else:
        print("\nOpção inválida ou saindo...")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--setup':
        setup_aws_credentials_interactive()
    else:
        print_credential_status()
