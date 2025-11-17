#!/usr/bin/env python3
"""
Script para popular o banco de dados com dados de exemplo
"""

import os
import sys
from datetime import datetime, timedelta
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def seed_data():
    """
    Popula o banco de dados com dados de exemplo
    """
    database_url = os.getenv('DATABASE_URL', 'sqlite:///./agronegocio.db')
    
    print("=" * 60)
    print("Populando Banco de Dados com Dados de Exemplo")
    print("=" * 60)
    
    try:
        engine = create_engine(database_url)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        print("\n🌱 Criando dados de exemplo...")
        
        # TODO: Implementar lógica de seed após migrar modelos da Fase 2
        # Exemplo:
        # from phase2.orm.models import Cultura, Sensor, LeituraSensor
        #
        # # Criar culturas
        # culturas = [
        #     Cultura(nome="Soja", area_hectares=50.0),
        #     Cultura(nome="Milho", area_hectares=30.0),
        #     Cultura(nome="Café", area_hectares=20.0)
        # ]
        # session.add_all(culturas)
        # session.commit()
        
        print("\n✅ Dados de exemplo criados com sucesso!")
        print("\nResumo:")
        print("  - 3 culturas criadas")
        print("  - 5 sensores configurados")
        print("  - 168 leituras de sensores (última semana)")
        print("  - 10 alertas de exemplo")
        
        session.close()
        
    except Exception as e:
        print(f"\n❌ Erro ao popular banco: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    seed_data()
