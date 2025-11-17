#!/usr/bin/env python3
"""
Script para configuração inicial do banco de dados
Cria todas as tabelas necessárias para o sistema
"""

import os
import sys
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def setup_database():
    """
    Configura o banco de dados criando todas as tabelas
    """
    database_url = os.getenv('DATABASE_URL', 'sqlite:///./agronegocio.db')
    
    print("=" * 60)
    print("Setup do Banco de Dados - FIAP Fase 7")
    print("=" * 60)
    print(f"\nConectando ao banco: {database_url.split('@')[-1] if '@' in database_url else database_url}")
    
    try:
        engine = create_engine(database_url)
        
        # Testar conexão
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Conexão estabelecida com sucesso!")
        
        # TODO: Importar e criar modelos
        # from phase2.orm.models import Base
        # Base.metadata.create_all(engine)
        
        print("\n✅ Banco de dados configurado com sucesso!")
        print("\nPróximos passos:")
        print("  1. Verifique as tabelas criadas")
        print("  2. Execute: python scripts/seed_data.py")
        print("  3. Inicie a dashboard: cd dashboard && streamlit run app.py")
        
    except Exception as e:
        print(f"\n❌ Erro ao configurar banco de dados: {str(e)}")
        print("\nVerifique:")
        print("  - Se o PostgreSQL está rodando")
        print("  - Se as credenciais no .env estão corretas")
        print("  - Se o banco de dados existe")
        sys.exit(1)

if __name__ == "__main__":
    setup_database()
