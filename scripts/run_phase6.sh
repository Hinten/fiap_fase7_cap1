#!/bin/bash
# Script para executar inferência YOLO (Fase 6)

echo "=========================================="
echo "Fase 6: Visão Computacional com YOLO"
echo "=========================================="
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

echo "📍 Diretório do projeto: $PROJECT_ROOT"
echo ""

# Verificar ambiente virtual
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "⚠️  Ambiente virtual não detectado"
    echo "Execute: source .venv/bin/activate"
    exit 1
fi

# Executar detecção YOLO
echo "👁️  Executando detecção YOLO..."
cd "$PROJECT_ROOT/phase6/inferencia"

if [ -f "detect.py" ]; then
    # Verificar se há imagens
    if [ -d "../images" ] && [ "$(ls -A ../images)" ]; then
        echo "Processando imagens em: ../images/"
        python detect.py --source ../images/ --conf 0.5 --save
        echo ""
        echo "✅ Inferência concluída"
        echo "   Resultados salvos em: runs/detect/"
    else
        echo "⚠️  Nenhuma imagem encontrada em phase6/images/"
        echo "    Adicione imagens para processar"
    fi
else
    echo "⚠️  detect.py não encontrado"
    echo "    Migre o código do repositório: https://github.com/Hinten/fiap_fase6_cap1"
fi

echo ""
echo "=========================================="
echo "Fase 6 concluída!"
echo "=========================================="
