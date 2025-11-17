# Fase 2: Banco de Dados Estruturado

## 📋 Descrição

Esta fase estrutura um banco de dados relacional completo (MER e DER) integrando dados de manejo agrícola.

## 🎯 Objetivos

- Modelo Entidade-Relacionamento (MER)
- Diagrama Entidade-Relacionamento (DER)
- Scripts SQL de criação e migração
- Modelos ORM com SQLAlchemy
- Integração com dados da Fase 1

## 📂 Estrutura

```
phase2/
├── modelos/         # MER e DER (diagramas)
├── scripts_sql/     # Scripts de criação e migração
└── orm/             # Modelos SQLAlchemy
```

## 🗄️ Schema do Banco de Dados

### Principais Tabelas

- **culturas**: Informações sobre cultivos
- **sensores**: Cadastro de sensores IoT
- **leituras_sensor**: Dados coletados pelos sensores
- **alertas**: Histórico de alertas emitidos
- **usuarios**: Usuários do sistema
- **acoes_corretivas**: Ações tomadas em resposta a alertas

## 🔧 Como Usar

### Setup Inicial

```bash
# Criar estrutura do banco
python scripts/setup_database.py

# Popular com dados de exemplo
python scripts/seed_data.py
```

### Migrations

```bash
# Criar nova migração
alembic revision --autogenerate -m "descrição"

# Aplicar migrações
alembic upgrade head
```

## 📦 Dependências Específicas

```
sqlalchemy
psycopg2-binary
alembic
```

## 🔗 Repositório Original

[fiap_fase2_cap1](https://github.com/treino258/fiap_fase2_cap1)

## 📝 O Que Trazer do Repositório Original

- Diagramas MER/DER (.png, .pdf)
- Scripts SQL de criação de tabelas
- Modelos ORM (models.py)
- Scripts de migração
- Dados de seed
