#!/bin/bash
# Script para executar serviços da Fase 1 (Meteorologia)

echo "=========================================="
echo "Fase 1: Base de Dados e Meteorologia"
echo "=========================================="
echo ""

# Diretório do script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

echo "📍 Diretório do projeto: $PROJECT_ROOT"
echo ""

# Verificar se o ambiente virtual está ativo
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "⚠️  Ambiente virtual não detectado"
    echo "Execute: source .venv/bin/activate"
    exit 1
fi

# Executar API meteorológica
echo "☁️  Buscando dados meteorológicos..."
cd "$PROJECT_ROOT/phase1/api_meteorologica"

if [ -f "fetch_weather.py" ]; then
    python fetch_weather.py
    echo "✅ Dados meteorológicos obtidos"
else
    echo "⚠️  fetch_weather.py não encontrado"
    echo "    Migre o código do repositório original: https://github.com/Hinten/fiap_fase1_cap1"
fi

echo ""

# Executar cálculos
echo "📊 Executando cálculos de área e insumos..."
cd "$PROJECT_ROOT/phase1/calculos"

if [ -f "calculos.py" ]; then
    python calculos.py
    echo "✅ Cálculos executados"
else
    echo "⚠️  calculos.py não encontrado"
fi

echo ""

# Executar análise estatística em R (se disponível)
echo "📈 Executando análise estatística em R..."
cd "$PROJECT_ROOT/phase1/analise_estatistica"

if command -v Rscript &> /dev/null; then
    if [ -f "analise.R" ]; then
        Rscript analise.R
        echo "✅ Análise R executada"
    else
        echo "⚠️  analise.R não encontrado"
    fi
else
    echo "⚠️  R não instalado, pulando análise estatística"
fi

echo ""
echo "=========================================="
echo "Fase 1 concluída!"
echo "=========================================="
