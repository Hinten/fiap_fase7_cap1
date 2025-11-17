#!/bin/bash
# Script para executar serviços da Fase 3 (IoT e Sensores)

echo "=========================================="
echo "Fase 3: IoT e Automação Inteligente"
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

# Iniciar simulador de sensores em background
echo "🤖 Iniciando simulador de sensores..."
cd "$PROJECT_ROOT/phase3/sensores"

if [ -f "simulador.py" ]; then
    python simulador.py &
    SENSOR_PID=$!
    echo "✅ Simulador iniciado (PID: $SENSOR_PID)"
else
    echo "⚠️  simulador.py não encontrado"
    echo "    Migre o código do repositório: https://github.com/Hinten/fiap_fase3_cap1-novo"
fi

echo ""
sleep 2

# Iniciar API CRUD
echo "🔌 Iniciando API CRUD..."
cd "$PROJECT_ROOT/phase3/api_crud"

if [ -f "app.py" ]; then
    python app.py &
    API_PID=$!
    echo "✅ API iniciada (PID: $API_PID)"
    echo "   Acesse: http://localhost:8000/docs"
else
    echo "⚠️  app.py não encontrado"
fi

echo ""
echo "=========================================="
echo "Serviços Fase 3 rodando!"
echo "=========================================="
echo ""
echo "Para parar os serviços:"
echo "  kill $SENSOR_PID $API_PID"
echo ""
echo "Pressione Ctrl+C para finalizar..."

# Aguardar Ctrl+C
trap "echo ''; echo 'Finalizando serviços...'; kill $SENSOR_PID $API_PID 2>/dev/null; exit 0" SIGINT SIGTERM

# Manter script rodando
wait
