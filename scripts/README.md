# Scripts Utilitários

Esta pasta contém scripts auxiliares para setup, manutenção e execução dos serviços.

## 📋 Scripts Disponíveis

### Setup e Configuração

- **setup_database.py** - Criação inicial das tabelas do banco de dados
- **seed_data.py** - Popular banco com dados de exemplo

### Execução de Serviços

- **run_phase1.sh** - Executar serviços da Fase 1 (meteorologia)
- **run_phase2.sh** - Executar operações de banco de dados
- **run_phase3.sh** - Iniciar simulador IoT e API
- **run_phase6.sh** - Executar inferência YOLO

### Manutenção

- **backup_database.sh** - Backup do banco de dados
- **restore_database.sh** - Restaurar backup
- **clean_logs.sh** - Limpar arquivos de log antigos

## 🚀 Como Usar

```bash
# Setup inicial
python setup_database.py
python seed_data.py

# Executar serviços
bash run_phase1.sh
bash run_phase3.sh
bash run_phase6.sh
```
