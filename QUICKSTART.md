# 🚀 Guia Rápido de Início - FarmTech Solutions

Este guia fornece instruções simples e rápidas para começar a usar o sistema FarmTech Solutions.

---

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1
```

### 2️⃣ Configurar Ambiente Python

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 3️⃣ Configurar Variáveis de Ambiente

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar com suas credenciais
nano .env  # ou use seu editor favorito
```

**Mínimo necessário para testar:**
```env
SQL_LITE=true
LOGGING_ENABLED=true
ENABLE_API=false

# AWS (opcional - para testar alertas)
# AWS_ACCESS_KEY_ID=sua_chave
# AWS_SECRET_ACCESS_KEY=sua_senha_secreta
# AWS_REGION=us-east-1
# SNS_TOPIC_ARN=arn:aws:sns:...
```

### 4️⃣ Testar o Sistema

```bash
# Testar CLI
python -m src.fase7.launcher --help

# Testar orquestrador
python -m src.fase7.orchestrator

# Testar AWS (se configurado)
python -m src.fase7.launcher --test-aws
```

---

## 📊 Executar Dashboard

### Opção A: Via Streamlit (quando implementado)

```bash
streamlit run src/fase4/streamlit_app.py
```

Acesse: `http://localhost:8501`

### Opção B: Via CLI

```bash
# Executar fase específica
python -m src.fase7.launcher --fase 5

# Executar todas as fases
python -m src.fase7.launcher --all

# Com saída detalhada
python -m src.fase7.launcher --fase 5 --verbose
```

---

## 🔌 API IoT (Fase 3)

### Iniciar API para ESP32

```bash
uvicorn src.fase3.api:app --reload --port 8180
```

### Endpoint de teste

```bash
curl -X POST http://localhost:8180/api/sensor/reading \
  -H "Content-Type: application/json" \
  -d '{
    "serial": "ESP32-TEST",
    "temperatura": 28.5,
    "umidade": 65.0,
    "ph": 6.8
  }'
```

---

## ☁️ Configurar AWS (Opcional)

### 1. Criar Tópico SNS

```bash
aws sns create-topic --name farm-alerts --region us-east-1
```

### 2. Adicionar Assinatura de Email

```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:SEU_ACCOUNT_ID:farm-alerts \
  --protocol email \
  --notification-endpoint seu-email@example.com
```

### 3. Confirmar Email

Verifique sua caixa de entrada e confirme a assinatura clicando no link.

### 4. Configurar .env

```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=abc123...
AWS_REGION=us-east-1
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789:farm-alerts
```

### 5. Testar

```bash
python -m src.fase7.launcher --test-aws
```

---

## 🧪 Exemplos de Uso

### Enviar Alerta AWS via Python

```python
from src.fase5.aws.alert_service import publish_alert

# Alerta simples
result = publish_alert(
    subject="Teste do Sistema",
    message="Este é um alerta de teste",
    severity="INFO"
)

print(result)
```

### Usar Orquestrador

```python
from src.fase7.orchestrator import run_phase

# Executar Fase 5
result = run_phase(5, send_test_alert=True)
print(result)
```

---

## 📁 Estrutura de Pastas

```
fiap_fase7_cap1/
├── README.md              # Documentação principal
├── roadmap.md             # Plano de integração
├── requirements.txt       # Dependências
├── .env.example           # Template de configuração
│
├── src/                   # Código fonte
│   ├── fase1/             # Cálculos agrícolas
│   ├── fase2/             # Banco de dados
│   ├── fase3/             # IoT e sensores
│   ├── fase4/             # Dashboard + ML
│   ├── fase5/aws/         # Alertas AWS ⭐
│   ├── fase6/             # YOLO
│   └── fase7/             # Orquestração ⭐
│
└── docs/                  # Documentação
    └── aws_screenshots/   # Prints AWS
```

---

## 🆘 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'boto3'"

```bash
pip install boto3
```

### Erro: "AWS credentials not configured"

Verifique se o arquivo `.env` existe e contém as credenciais AWS:

```bash
cat .env | grep AWS
```

### Erro: "Permission denied"

No Linux/Mac, torne os scripts executáveis:

```bash
chmod +x src/fase7/launcher.py
```

### Dashboard não inicia

Verifique se o Streamlit está instalado:

```bash
pip install streamlit
streamlit hello  # Teste básico
```

---

## 📚 Documentação Completa

- **README.md** - Visão geral do sistema
- **roadmap.md** - Plano de integração detalhado
- **src/fase5/aws/iam_policy.md** - Configuração AWS
- **src/fase5/aws/infra_notes.md** - Deploy em produção

---

## 🤝 Suporte

- **Issues:** [GitHub Issues](https://github.com/Hinten/fiap_fase7_cap1/issues)
- **Email:** contato@farmtech.com.br
- **Documentação:** Ver README.md completo

---

## ✅ Checklist de Configuração

- [ ] Python 3.11+ instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` criado e configurado
- [ ] Testes básicos executados com sucesso
- [ ] AWS configurado (opcional mas recomendado)
- [ ] Dashboard funcional (quando implementado)

---

**Pronto para começar! 🚀**

Para dúvidas, consulte o README.md completo ou abra uma issue no GitHub.
