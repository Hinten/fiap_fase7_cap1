# 🗺️ Roadmap - Fase 7: Consolidação do Sistema de Gestão para Agronegócio

## 📋 Visão Geral

Este documento descreve todos os passos necessários para integrar as Fases 1 a 6 do projeto FIAP em um sistema consolidado de gestão para agronegócio, conforme os requisitos da Fase 7.

---

## 🎯 Objetivos da Fase 7

1. **Integração Completa:** Reunir todos os serviços desenvolvidos nas Fases 1-6 em uma única pasta de projeto
2. **Dashboard Unificada:** Aprimorar a dashboard da Fase 4 para disparar serviços via botões/comandos
3. **Sistema de Alertas:** Implementar mensageria AWS (SNS/SES) para notificações automáticas
4. **Documentação:** Criar documentação completa com prints, instruções e vídeo demonstrativo
5. **Entrega:** Repositório GitHub organizado e vídeo de até 10 minutos

---

## 📅 Cronograma Sugerido

### Semana 1: Preparação e Inventário
- Clonar e analisar todos os repositórios anteriores
- Inventariar código, dependências e funcionalidades
- Definir arquitetura de integração

### Semana 2: Estruturação do Projeto
- Criar estrutura de pastas consolidada
- Migrar código das Fases 1-6
- Normalizar dependências e configurações

### Semana 3: Desenvolvimento da Dashboard Unificada
- Desenvolver interface principal
- Integrar serviços com botões/comandos
- Implementar visualizações consolidadas

### Semana 4: Sistema de Mensageria AWS
- Configurar SNS e SES
- Desenvolver função Lambda
- Integrar triggers de alertas

### Semana 5: Testes e Documentação
- Testar todas as funcionalidades
- Capturar screenshots AWS
- Criar documentação completa

### Semana 6: Finalização
- Gravar vídeo de apresentação
- Revisão final
- Entrega do projeto

---

## 🔍 Fase 1: Inventário e Análise dos Repositórios

### 1.1. Clonar Repositórios Originais

```bash
# Criar pasta temporária para análise
mkdir ~/temp_analysis
cd ~/temp_analysis

# Clonar cada repositório
git clone https://github.com/Hinten/fiap_fase1_cap1.git
git clone https://github.com/treino258/fiap_fase2_cap1.git
git clone https://github.com/Hinten/fiap_fase3_cap1-novo.git
git clone https://github.com/Al1ce4-AI/fiap_fase4_cap1.git
git clone https://github.com/Hinten/fiap_fase5_cap1.git
git clone https://github.com/Hinten/fiap_fase6_cap1.git
```

### 1.2. Inventariar Fase 1 - Base de Dados Inicial

**O que extrair:**
- [ ] Scripts Python para cálculos de área de plantio
- [ ] Scripts Python para gestão de insumos
- [ ] Código de integração com API meteorológica
- [ ] Scripts R para análise estatística
- [ ] Notebooks Jupyter (se existirem)
- [ ] Dados de exemplo (CSV, JSON)
- [ ] Dependências (requirements.txt)
- [ ] Documentação README

**Arquivos-chave esperados:**
- `calculos_area.py`
- `gestao_insumos.py`
- `api_meteorologica.py`
- `analise_estatistica.R`
- `dados_exemplo.csv`

**Dependências esperadas:**
- requests (para API)
- pandas, numpy
- matplotlib, seaborn
- R packages: tidyverse, ggplot2, forecast

### 1.3. Inventariar Fase 2 - Banco de Dados Estruturado

**O que extrair:**
- [ ] Diagramas MER e DER (imagens/PDF)
- [ ] Scripts SQL de criação de tabelas
- [ ] Scripts de migração
- [ ] Modelos ORM (SQLAlchemy/Django)
- [ ] Scripts de seed/população do BD
- [ ] Consultas SQL comuns
- [ ] Documentação do schema

**Arquivos-chave esperados:**
- `MER.png` / `DER.png`
- `create_tables.sql`
- `models.py` (SQLAlchemy)
- `migrations/`
- `seed_data.sql`

**Dependências esperadas:**
- SQLAlchemy
- psycopg2-binary (PostgreSQL)
- alembic (migrações)

### 1.4. Inventariar Fase 3 - IoT e Automação

**O que extrair:**
- [ ] Firmware ESP32 (.ino para Arduino IDE)
- [ ] Código de leitura de sensores (DHT22, LDR)
- [ ] Lógica de acionamento de irrigação
- [ ] API REST (Flask/FastAPI) para CRUD
- [ ] Simuladores de sensores (para testes sem hardware)
- [ ] Scripts de integração com BD
- [ ] Configurações de rede/WiFi

**Arquivos-chave esperados:**
- `esp32_firmware/main.ino`
- `sensor_dht22.py`
- `sensor_ldr.py`
- `api_crud.py` (Flask/FastAPI)
- `simulador_sensores.py`
- `logica_irrigacao.py`

**Dependências esperadas:**
- Flask ou FastAPI
- requests
- paho-mqtt (se usar MQTT)
- Adafruit_DHT (para leitura de sensores)

### 1.5. Inventariar Fase 4 - Dashboard com Data Science

**O que extrair:**
- [ ] Aplicação Streamlit completa
- [ ] Modelos de Machine Learning treinados (.pkl, .joblib)
- [ ] Notebooks de treinamento
- [ ] Scripts de pré-processamento de dados
- [ ] Visualizações e gráficos
- [ ] Código de integração com ESP32 (LCD, Serial Plotter)
- [ ] Algoritmos preditivos

**Arquivos-chave esperados:**
- `streamlit_app.py`
- `modelo_regressao.pkl`
- `modelo_classificacao.pkl`
- `preprocessing.py`
- `visualizacoes.py`
- `notebooks/treinamento.ipynb`

**Dependências esperadas:**
- streamlit
- scikit-learn
- pandas, numpy
- plotly, matplotlib
- joblib

### 1.6. Inventariar Fase 5 - Cloud Computing & Segurança

**O que extrair:**
- [ ] Templates CloudFormation ou Terraform
- [ ] Scripts de deploy AWS
- [ ] Configurações de segurança (IAM policies)
- [ ] Documentação de arquitetura AWS
- [ ] Scripts de backup e restauração
- [ ] Configurações de monitoramento (CloudWatch)
- [ ] Documentação ISO 27001/27002

**Arquivos-chave esperados:**
- `cloudformation_template.yaml` ou `terraform/main.tf`
- `deploy_aws.sh`
- `iam_policies.json`
- `backup_script.sh`
- `docs/arquitetura_aws.md`
- `docs/seguranca_iso.md`

**Dependências esperadas:**
- boto3 (AWS SDK para Python)
- awscli

### 1.7. Inventariar Fase 6 - Visão Computacional

**O que extrair:**
- [ ] Modelo YOLO treinado (pesos .pt ou .weights)
- [ ] Scripts de inferência/detecção
- [ ] Dataset de imagens (ou pasta de exemplos)
- [ ] Código de treinamento (se disponível)
- [ ] Script de integração com ESP32-CAM
- [ ] Notebooks de análise de resultados
- [ ] Classes detectadas (labels.txt)

**Arquivos-chave esperados:**
- `modelo_yolo/best.pt`
- `detect.py` (inferência)
- `images/` (imagens de teste)
- `train.py` (treinamento)
- `labels.txt` (classes)
- `esp32_cam_integration.py`

**Dependências esperadas:**
- torch, torchvision
- ultralytics (YOLOv8) ou yolov5
- opencv-python
- pillow

---

## 🏗️ Fase 2: Estruturação do Projeto Consolidado

### 2.1. Criar Estrutura de Pastas

```bash
# No repositório consolidado fiap_fase7_cap1
mkdir -p phase1/{calculos,api_meteorologica,analise_estatistica}
mkdir -p phase2/{modelos,scripts_sql,orm}
mkdir -p phase3/{firmware_esp32,sensores,api_crud}
mkdir -p phase4/{streamlit_app,modelos_ml,notebooks}
mkdir -p phase5/{infraestrutura,scripts_deploy,seguranca}
mkdir -p phase6/{modelo_yolo,inferencia,images}
mkdir -p dashboard/{pages,components,utils}
mkdir -p aws_alerts/{templates}
mkdir -p scripts
mkdir -p data/{samples,images,exports}
mkdir -p docs/{aws_screenshots}
```

### 2.2. Migrar Código das Fases

**Fase 1:**
```bash
cp ~/temp_analysis/fiap_fase1_cap1/calculos*.py phase1/calculos/
cp ~/temp_analysis/fiap_fase1_cap1/api_*.py phase1/api_meteorologica/
cp ~/temp_analysis/fiap_fase1_cap1/*.R phase1/analise_estatistica/
cp ~/temp_analysis/fiap_fase1_cap1/README.md phase1/
```

**Fase 2:**
```bash
cp ~/temp_analysis/fiap_fase2_cap1/*.png phase2/modelos/
cp ~/temp_analysis/fiap_fase2_cap1/*.sql phase2/scripts_sql/
cp ~/temp_analysis/fiap_fase2_cap1/models.py phase2/orm/
cp ~/temp_analysis/fiap_fase2_cap1/README.md phase2/
```

**Fase 3:**
```bash
cp -r ~/temp_analysis/fiap_fase3_cap1-novo/esp32_code phase3/firmware_esp32/
cp ~/temp_analysis/fiap_fase3_cap1-novo/sensor*.py phase3/sensores/
cp ~/temp_analysis/fiap_fase3_cap1-novo/api*.py phase3/api_crud/
cp ~/temp_analysis/fiap_fase3_cap1-novo/README.md phase3/
```

**Fase 4:**
```bash
cp -r ~/temp_analysis/fiap_fase4_cap1/streamlit_app/* phase4/streamlit_app/
cp ~/temp_analysis/fiap_fase4_cap1/*.pkl phase4/modelos_ml/
cp ~/temp_analysis/fiap_fase4_cap1/notebooks/*.ipynb phase4/notebooks/
cp ~/temp_analysis/fiap_fase4_cap1/README.md phase4/
```

**Fase 5:**
```bash
cp -r ~/temp_analysis/fiap_fase5_cap1/cloudformation/* phase5/infraestrutura/
cp ~/temp_analysis/fiap_fase5_cap1/deploy*.sh phase5/scripts_deploy/
cp -r ~/temp_analysis/fiap_fase5_cap1/docs/* phase5/seguranca/
cp ~/temp_analysis/fiap_fase5_cap1/README.md phase5/
```

**Fase 6:**
```bash
cp ~/temp_analysis/fiap_fase6_cap1/modelo/*.pt phase6/modelo_yolo/
cp ~/temp_analysis/fiap_fase6_cap1/detect.py phase6/inferencia/
cp -r ~/temp_analysis/fiap_fase6_cap1/images/* phase6/images/
cp ~/temp_analysis/fiap_fase6_cap1/README.md phase6/
```

### 2.3. Consolidar Dependências

Criar `requirements.txt` consolidado:

```bash
# Coletar todos os requirements
cat ~/temp_analysis/fiap_fase1_cap1/requirements.txt > /tmp/all_reqs.txt
cat ~/temp_analysis/fiap_fase2_cap1/requirements.txt >> /tmp/all_reqs.txt
cat ~/temp_analysis/fiap_fase3_cap1-novo/requirements.txt >> /tmp/all_reqs.txt
cat ~/temp_analysis/fiap_fase4_cap1/requirements.txt >> /tmp/all_reqs.txt
cat ~/temp_analysis/fiap_fase5_cap1/requirements.txt >> /tmp/all_reqs.txt
cat ~/temp_analysis/fiap_fase6_cap1/requirements.txt >> /tmp/all_reqs.txt

# Remover duplicatas e criar requirements.txt final
sort /tmp/all_reqs.txt | uniq > requirements.txt
```

Conteúdo esperado do `requirements.txt`:

```txt
# Core
python-dotenv==1.0.0
pyyaml==6.0

# Web Framework
streamlit==1.28.0
fastapi==0.104.1
uvicorn==0.24.0
flask==3.0.0

# Database
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
alembic==1.12.1

# Data Analysis
pandas==2.1.3
numpy==1.26.2
scipy==1.11.4

# Machine Learning
scikit-learn==1.3.2
joblib==1.3.2

# Computer Vision
torch==2.1.0
torchvision==0.16.0
ultralytics==8.0.206
opencv-python==4.8.1
pillow==10.1.0

# Visualization
matplotlib==3.8.2
seaborn==0.13.0
plotly==5.18.0

# AWS
boto3==1.29.7
awscli==1.30.7

# IoT/Sensors
requests==2.31.0
paho-mqtt==1.6.1

# Development
pytest==7.4.3
black==23.11.0
flake8==6.1.0
```

### 2.4. Criar Arquivo .env.example

```bash
cat > .env.example << 'EOF'
# =============================================================================
# CONFIGURAÇÕES DE AMBIENTE - FASE 7
# =============================================================================
# Copie este arquivo para .env e preencha com suas credenciais

# -----------------------------------------------------------------------------
# Banco de Dados
# -----------------------------------------------------------------------------
# Para PostgreSQL:
DATABASE_URL=postgresql://usuario:senha@localhost:5432/agronegocio

# Para SQLite (desenvolvimento local):
# DATABASE_URL=sqlite:///./agronegocio.db

# -----------------------------------------------------------------------------
# API Meteorológica (Fase 1)
# -----------------------------------------------------------------------------
WEATHER_API_KEY=sua_chave_api_aqui
WEATHER_API_URL=https://api.openweathermap.org/data/2.5
WEATHER_API_LOCATION=Sao Paulo,BR

# -----------------------------------------------------------------------------
# AWS Credentials (Fase 5)
# -----------------------------------------------------------------------------
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=us-east-1

# -----------------------------------------------------------------------------
# Amazon SNS - SMS (Sistema de Alertas)
# -----------------------------------------------------------------------------
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789012:alertas-fazenda
SNS_PHONE_NUMBERS=+5511999999999,+5511988888888

# -----------------------------------------------------------------------------
# Amazon SES - E-mail (Sistema de Alertas)
# -----------------------------------------------------------------------------
SES_SENDER_EMAIL=noreply@suafazenda.com.br
SES_SENDER_NAME=Sistema de Alertas - Fazenda
SES_RECIPIENT_EMAILS=gestor@suafazenda.com.br,operador@suafazenda.com.br

# -----------------------------------------------------------------------------
# ESP32 IoT (Fase 3)
# -----------------------------------------------------------------------------
ESP32_ENABLED=false
ESP32_IP_ADDRESS=192.168.1.100
ESP32_API_ENDPOINT=http://192.168.1.100/api
ESP32_MQTT_BROKER=mqtt.fazenda.local
ESP32_MQTT_PORT=1883

# -----------------------------------------------------------------------------
# Sensores - Limiares de Alerta (Fase 3)
# -----------------------------------------------------------------------------
SENSOR_UMIDADE_MIN=30.0
SENSOR_UMIDADE_MAX=80.0
SENSOR_TEMPERATURA_MIN=15.0
SENSOR_TEMPERATURA_MAX=35.0
SENSOR_LUZ_MIN=200
SENSOR_LUZ_MAX=800

# -----------------------------------------------------------------------------
# YOLO - Visão Computacional (Fase 6)
# -----------------------------------------------------------------------------
YOLO_MODEL_PATH=./phase6/modelo_yolo/best.pt
YOLO_CONFIDENCE_THRESHOLD=0.5
YOLO_IOU_THRESHOLD=0.45
YOLO_IMAGE_SIZE=640

# -----------------------------------------------------------------------------
# Dashboard (Fase 4)
# -----------------------------------------------------------------------------
DASHBOARD_PORT=8501
DASHBOARD_TITLE=Sistema de Gestão Agronegócio - FIAP Fase 7
DASHBOARD_REFRESH_INTERVAL=30

# -----------------------------------------------------------------------------
# Machine Learning (Fase 4)
# -----------------------------------------------------------------------------
ML_MODEL_REGRESSAO_PATH=./phase4/modelos_ml/modelo_regressao.pkl
ML_MODEL_CLASSIFICACAO_PATH=./phase4/modelos_ml/modelo_classificacao.pkl
ML_RETRAIN_INTERVAL_DAYS=30

# -----------------------------------------------------------------------------
# Logs e Debug
# -----------------------------------------------------------------------------
LOG_LEVEL=INFO
DEBUG_MODE=false
EOF
```

### 2.5. Criar .gitignore

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Ambiente
.env
.env.local
.env.*.local
*.log

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Jupyter
.ipynb_checkpoints/
*.ipynb

# Dados sensíveis
*.pem
*.key
*.crt
credentials.json
secrets.yaml

# AWS
.aws/
*.pem

# Banco de Dados
*.db
*.sqlite
*.sqlite3

# Modelos grandes
*.pt
*.pth
*.h5
*.pkl
!phase4/modelos_ml/*.pkl
!phase6/modelo_yolo/best.pt

# Imagens e vídeos grandes
*.mp4
*.avi
!docs/aws_screenshots/*.png

# Temporários
/tmp/
temp/
*.tmp
*.bak

# OS
.DS_Store
Thumbs.db
EOF
```

---

## 🎨 Fase 3: Desenvolvimento da Dashboard Unificada

### 3.1. Criar Estrutura da Dashboard

```bash
cd dashboard

# Criar páginas
touch pages/home.py
touch pages/fase1_meteorologia.py
touch pages/fase2_banco_dados.py
touch pages/fase3_iot.py
touch pages/fase4_ml.py
touch pages/fase6_visao.py
touch pages/alertas.py

# Criar componentes
touch components/sidebar.py
touch components/charts.py
touch components/sensors.py
touch components/metrics.py

# Criar utilitários
touch utils/database.py
touch utils/aws_client.py
touch utils/sensor_simulator.py
touch utils/yolo_inference.py
```

### 3.2. Implementar app.py Principal

**Estrutura do arquivo `dashboard/app.py`:**

```python
import streamlit as st
import subprocess
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="FIAP Fase 7 - Agronegócio",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar com navegação
st.sidebar.title("🌱 Sistema de Gestão")
st.sidebar.markdown("---")

# Menu de navegação
page = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Home",
        "☁️ Fase 1: Meteorologia",
        "🗄️ Fase 2: Banco de Dados",
        "🤖 Fase 3: IoT e Sensores",
        "📊 Fase 4: Machine Learning",
        "👁️ Fase 6: Visão Computacional",
        "📧 Sistema de Alertas"
    ]
)

# Botões de ação rápida
st.sidebar.markdown("---")
st.sidebar.subheader("Ações Rápidas")

if st.sidebar.button("▶️ Iniciar Sensores"):
    subprocess.Popen(["python", "../phase3/sensores/simulador.py"])
    st.sidebar.success("Sensores iniciados!")

if st.sidebar.button("📸 Processar Imagens"):
    subprocess.Popen(["python", "../phase6/inferencia/detect.py"])
    st.sidebar.success("Processamento iniciado!")

if st.sidebar.button("🚨 Enviar Alerta Teste"):
    subprocess.Popen(["python", "../aws_alerts/send_test_alert.py"])
    st.sidebar.success("Alerta enviado!")

# Conteúdo principal baseado na página selecionada
if page == "🏠 Home":
    from pages import home
    home.render()
elif page == "☁️ Fase 1: Meteorologia":
    from pages import fase1_meteorologia
    fase1_meteorologia.render()
# ... outras páginas
```

### 3.3. Implementar Páginas

**Cada página deve:**
- [ ] Ter título e descrição clara
- [ ] Mostrar métricas relevantes
- [ ] Permitir interação com o serviço
- [ ] Exibir visualizações (gráficos, tabelas)
- [ ] Ter botões para executar ações
- [ ] Integrar com banco de dados
- [ ] Capturar e exibir logs/status

### 3.4. Integrar Serviços

**Métodos de integração:**

1. **Subprocess (para scripts independentes):**
```python
import subprocess
result = subprocess.run(["python", "../phase1/api_meteorologica.py"], 
                       capture_output=True, text=True)
st.write(result.stdout)
```

2. **Import direto (para funções Python):**
```python
import sys
sys.path.append("../phase3")
from api_crud import get_sensor_data
data = get_sensor_data()
```

3. **API REST (para serviços rodando):**
```python
import requests
response = requests.get("http://localhost:5000/api/sensors")
data = response.json()
```

---

## 🔔 Fase 4: Sistema de Mensageria AWS

### 4.1. Configurar Amazon SNS (SMS)

**Passo 1: Criar tópico SNS via AWS Console**

1. Acesse AWS Console → SNS
2. Clique em "Create topic"
3. Tipo: Standard
4. Nome: `alertas-fazenda`
5. Display name: `Alertas Fazenda`
6. Copie o ARN gerado

**Passo 2: Subscrever número de telefone**

```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:alertas-fazenda \
  --protocol sms \
  --notification-endpoint +5511999999999
```

**Passo 3: Configurar permissões de SMS**

1. SNS → Text messaging (SMS)
2. SMS preferences
3. Default message type: Transactional
4. Monthly spending limit: $10.00

**Capturar screenshots:**
- [ ] `docs/aws_screenshots/sns_topic_creation.png`
- [ ] `docs/aws_screenshots/sns_subscription.png`
- [ ] `docs/aws_screenshots/sns_permissions.png`

### 4.2. Configurar Amazon SES (E-mail)

**Passo 1: Verificar e-mail remetente**

```bash
aws ses verify-email-identity --email-address noreply@suafazenda.com.br
```

Ou via console:
1. AWS Console → SES → Verified identities
2. Create identity
3. Email address: `noreply@suafazenda.com.br`
4. Verificar caixa de entrada e clicar no link

**Passo 2: Verificar e-mails destinatários (sandbox)**

```bash
aws ses verify-email-identity --email-address gestor@suafazenda.com.br
```

**Passo 3: Solicitar saída do sandbox (produção)**

1. SES → Account dashboard
2. Request production access
3. Preencher formulário justificando uso

**Passo 4: Criar template de e-mail**

```bash
aws ses create-template --cli-input-json file://email_template.json
```

`email_template.json`:
```json
{
  "Template": {
    "TemplateName": "AlertaFazenda",
    "SubjectPart": "🚨 Alerta - {{tipo_alerta}}",
    "TextPart": "Alerta detectado: {{mensagem}}",
    "HtmlPart": "<html><body><h1>{{tipo_alerta}}</h1><p>{{mensagem}}</p></body></html>"
  }
}
```

**Capturar screenshots:**
- [ ] `docs/aws_screenshots/ses_verified_identities.png`
- [ ] `docs/aws_screenshots/ses_template.png`
- [ ] `docs/aws_screenshots/ses_sandbox_status.png`

### 4.3. Criar Função Lambda

**Arquivo: `aws_alerts/lambda_handler.py`**

```python
import json
import boto3
import os
from datetime import datetime

# Clientes AWS
sns_client = boto3.client('sns')
ses_client = boto3.client('ses')

# Configurações
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
SES_SENDER = os.environ['SES_SENDER_EMAIL']
SES_RECIPIENTS = os.environ['SES_RECIPIENT_EMAILS'].split(',')

def lambda_handler(event, context):
    """
    Processar alertas e enviar notificações via SNS e SES
    """
    try:
        # Parsear evento
        alert_data = json.loads(event['body']) if 'body' in event else event
        
        tipo_alerta = alert_data.get('tipo', 'Desconhecido')
        mensagem = alert_data.get('mensagem', '')
        severidade = alert_data.get('severidade', 'INFO')
        setor = alert_data.get('setor', 'N/A')
        valor = alert_data.get('valor', '')
        
        # Construir mensagens
        sms_message = f"⚠️ {tipo_alerta}: {mensagem}. Setor: {setor}"
        
        email_subject = f"🚨 Alerta - {tipo_alerta}"
        email_body = f"""
        <html>
        <body>
            <h2>Alerta Detectado</h2>
            <p><strong>Tipo:</strong> {tipo_alerta}</p>
            <p><strong>Severidade:</strong> {severidade}</p>
            <p><strong>Setor:</strong> {setor}</p>
            <p><strong>Valor:</strong> {valor}</p>
            <p><strong>Mensagem:</strong> {mensagem}</p>
            <p><strong>Horário:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <hr>
            <p>Dashboard: https://dashboard.suafazenda.com.br</p>
        </body>
        </html>
        """
        
        # Enviar SMS via SNS
        sns_response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=sms_message,
            Subject=tipo_alerta
        )
        
        # Enviar e-mail via SES
        ses_response = ses_client.send_email(
            Source=SES_SENDER,
            Destination={'ToAddresses': SES_RECIPIENTS},
            Message={
                'Subject': {'Data': email_subject},
                'Body': {'Html': {'Data': email_body}}
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Alertas enviados com sucesso',
                'sns_message_id': sns_response['MessageId'],
                'ses_message_id': ses_response['MessageId']
            })
        }
        
    except Exception as e:
        print(f"Erro ao processar alerta: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

**Deploy da Lambda:**

```bash
cd aws_alerts

# Empacotar
zip -r lambda_function.zip lambda_handler.py

# Criar função
aws lambda create-function \
  --function-name ProcessarAlertasFazenda \
  --runtime python3.9 \
  --role arn:aws:iam::123456789012:role/lambda-execution-role \
  --handler lambda_handler.lambda_handler \
  --zip-file fileb://lambda_function.zip \
  --environment Variables="{SNS_TOPIC_ARN=$SNS_TOPIC_ARN,SES_SENDER_EMAIL=$SES_SENDER_EMAIL,SES_RECIPIENT_EMAILS=$SES_RECIPIENT_EMAILS}"

# Criar API Gateway (opcional)
aws apigatewayv2 create-api \
  --name alertas-api \
  --protocol-type HTTP \
  --target arn:aws:lambda:us-east-1:123456789012:function:ProcessarAlertasFazenda
```

**Capturar screenshots:**
- [ ] `docs/aws_screenshots/lambda_function.png`
- [ ] `docs/aws_screenshots/lambda_permissions.png`
- [ ] `docs/aws_screenshots/lambda_test.png`
- [ ] `docs/aws_screenshots/api_gateway.png`

### 4.4. Configurar Triggers

**Opção 1: CloudWatch Events (Cron)**

```bash
# Executar a cada 5 minutos
aws events put-rule \
  --name MonitorarSensores \
  --schedule-expression "rate(5 minutes)"

aws events put-targets \
  --rule MonitorarSensores \
  --targets "Id"="1","Arn"="arn:aws:lambda:us-east-1:123456789012:function:ProcessarAlertasFazenda"
```

**Opção 2: API Gateway (HTTP)**

Endpoint criado automaticamente, chamar via:
```python
import requests
response = requests.post(
    "https://xyz123.execute-api.us-east-1.amazonaws.com/alertas",
    json={
        "tipo": "Umidade Baixa",
        "mensagem": "Umidade do solo abaixo de 30%",
        "severidade": "CRITICAL",
        "setor": "Setor A",
        "valor": "25%"
    }
)
```

**Opção 3: DynamoDB Streams (Automático)**

Configurar trigger para inserções na tabela de alertas.

### 4.5. Implementar Integração na Dashboard

**Arquivo: `dashboard/pages/alertas.py`**

```python
import streamlit as st
import requests
import os

def render():
    st.title("📧 Sistema de Alertas AWS")
    
    # Formulário para enviar alerta manual
    with st.form("enviar_alerta"):
        st.subheader("Enviar Alerta Manual")
        
        tipo = st.selectbox("Tipo de Alerta", [
            "Umidade Baixa",
            "Temperatura Alta",
            "Praga Detectada",
            "Falha de Sensor"
        ])
        
        mensagem = st.text_area("Mensagem")
        severidade = st.select_slider("Severidade", ["INFO", "WARNING", "CRITICAL"])
        setor = st.text_input("Setor")
        
        submitted = st.form_submit_button("🚨 Enviar Alerta")
        
        if submitted:
            # Chamar Lambda via API Gateway
            api_url = os.getenv("AWS_LAMBDA_API_URL")
            payload = {
                "tipo": tipo,
                "mensagem": mensagem,
                "severidade": severidade,
                "setor": setor
            }
            
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                st.success("✅ Alerta enviado com sucesso!")
            else:
                st.error(f"❌ Erro ao enviar alerta: {response.text}")
    
    # Histórico de alertas
    st.subheader("Histórico de Alertas")
    # Carregar do banco de dados
    # ...
```

---

## 📝 Fase 5: Scripts Auxiliares

### 5.1. Script de Setup do Banco de Dados

**Arquivo: `scripts/setup_database.py`**

```python
#!/usr/bin/env python3
"""
Script para configuração inicial do banco de dados
"""
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import sys

# Adicionar diretório phase2 ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '../phase2'))
from orm.models import Base

def setup_database():
    load_dotenv()
    
    database_url = os.getenv('DATABASE_URL')
    
    print(f"Conectando ao banco: {database_url}")
    engine = create_engine(database_url)
    
    print("Criando tabelas...")
    Base.metadata.create_all(engine)
    
    print("✅ Banco de dados configurado com sucesso!")

if __name__ == "__main__":
    setup_database()
```

### 5.2. Scripts de Execução por Fase

**Arquivo: `scripts/run_phase1.sh`**

```bash
#!/bin/bash
echo "🌤️ Executando Fase 1: Meteorologia"
cd "$(dirname "$0")/../phase1/api_meteorologica"
python fetch_weather.py
python process_data.py
cd ../analise_estatistica
Rscript analise.R
echo "✅ Fase 1 concluída"
```

**Arquivo: `scripts/run_phase3.sh`**

```bash
#!/bin/bash
echo "🤖 Executando Fase 3: IoT"
cd "$(dirname "$0")/../phase3"
python sensores/simulador.py &
sleep 2
python api_crud/app.py &
echo "✅ Sensores e API iniciados"
echo "PID Simulador: $!"
```

**Arquivo: `scripts/run_phase6.sh`**

```bash
#!/bin/bash
echo "👁️ Executando Fase 6: Visão Computacional"
cd "$(dirname "$0")/../phase6/inferencia"
python detect.py --source ../images --conf 0.5
echo "✅ Inferência concluída"
```

### 5.3. Script de Seed de Dados

**Arquivo: `scripts/seed_data.py`**

```python
#!/usr/bin/env python3
"""
Popular banco de dados com dados de exemplo
"""
import os
from datetime import datetime, timedelta
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../phase2'))
from orm.models import Sensor, LeituraSensor, Cultura

def seed_data():
    load_dotenv()
    engine = create_engine(os.getenv('DATABASE_URL'))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("Populando banco de dados...")
    
    # Criar culturas
    culturas = [
        Cultura(nome="Soja", area_hectares=50.0),
        Cultura(nome="Milho", area_hectares=30.0),
        Cultura(nome="Café", area_hectares=20.0)
    ]
    session.add_all(culturas)
    
    # Criar sensores
    sensores = [
        Sensor(tipo="DHT22", localizacao="Setor A"),
        Sensor(tipo="DHT22", localizacao="Setor B"),
        Sensor(tipo="LDR", localizacao="Setor A")
    ]
    session.add_all(sensores)
    session.commit()
    
    # Gerar leituras dos últimos 7 dias
    print("Gerando leituras de sensores...")
    for sensor in sensores:
        for i in range(7 * 24):  # 7 dias, 1 leitura por hora
            timestamp = datetime.now() - timedelta(hours=i)
            
            if sensor.tipo == "DHT22":
                temperatura = random.uniform(18, 32)
                umidade = random.uniform(35, 75)
            else:
                temperatura = None
                umidade = None
            
            leitura = LeituraSensor(
                sensor_id=sensor.id,
                timestamp=timestamp,
                temperatura=temperatura,
                umidade=umidade,
                luminosidade=random.randint(200, 900) if sensor.tipo == "LDR" else None
            )
            session.add(leitura)
    
    session.commit()
    print(f"✅ {len(sensores)} sensores e {7*24*len(sensores)} leituras criados")

if __name__ == "__main__":
    seed_data()
```

---

## 📚 Fase 6: Documentação Completa

### 6.1. Criar README.md para Cada Fase

Cada pasta `phaseN/` deve ter um README.md explicando:
- [ ] O que foi desenvolvido nesta fase
- [ ] Tecnologias utilizadas
- [ ] Como executar isoladamente
- [ ] Dependências específicas
- [ ] Exemplos de uso

### 6.2. Documentar Arquitetura

**Arquivo: `docs/arquitetura.md`**

Conteúdo:
- [ ] Diagrama de arquitetura geral
- [ ] Fluxo de dados entre componentes
- [ ] Tecnologias por camada
- [ ] Integração AWS
- [ ] Segurança e autenticação

### 6.3. Capturar Screenshots AWS

**Checklist de screenshots necessários:**

- [ ] `docs/aws_screenshots/sns_topic_creation.png`
- [ ] `docs/aws_screenshots/sns_subscription.png`
- [ ] `docs/aws_screenshots/sns_test_message.png`
- [ ] `docs/aws_screenshots/ses_verified_identities.png`
- [ ] `docs/aws_screenshots/ses_template.png`
- [ ] `docs/aws_screenshots/lambda_function.png`
- [ ] `docs/aws_screenshots/lambda_environment_variables.png`
- [ ] `docs/aws_screenshots/lambda_test_event.png`
- [ ] `docs/aws_screenshots/lambda_execution_logs.png`
- [ ] `docs/aws_screenshots/api_gateway_routes.png`
- [ ] `docs/aws_screenshots/cloudwatch_logs.png`
- [ ] `docs/aws_screenshots/iam_role.png`
- [ ] `docs/aws_screenshots/email_received.png`
- [ ] `docs/aws_screenshots/sms_received.png`

### 6.4. Criar Guia de Instalação Detalhado

**Arquivo: `docs/instalacao_detalhada.md`**

Seções:
- [ ] Requisitos de sistema
- [ ] Instalação do Python e dependências
- [ ] Configuração do PostgreSQL
- [ ] Instalação do R
- [ ] Configuração AWS (passo a passo)
- [ ] Configuração do ESP32 (se aplicável)
- [ ] Troubleshooting comum

---

## 🎬 Fase 7: Gravação do Vídeo

### 7.1. Preparar Roteiro

**Arquivo: `docs/video_roteiro.md`**

```markdown
# Roteiro do Vídeo de Apresentação - Fase 7

**Duração Total:** Máximo 10 minutos

## Estrutura

### 1. Introdução (1 minuto)
- Apresentação do grupo
- Contextualização: Fases 1-6
- Objetivo da Fase 7: consolidação

**Script sugerido:**
"Olá, somos o grupo [Nome] e este é nosso projeto final da Fase 7. 
Ao longo das fases anteriores, desenvolvemos diversos módulos para 
gestão de agronegócio. Nesta fase, integramos tudo em um sistema único."

### 2. Estrutura do Projeto (1 minuto)
- Mostrar repositório GitHub
- Explicar organização de pastas
- Destacar principais arquivos

**O que mostrar:**
- Estrutura de pastas no VS Code
- README.md principal
- requirements.txt

### 3. Dashboard Unificada (3 minutos)
- Inicializar aplicação
- Navegar pelas páginas
- Demonstrar botões de ação

**Funcionalidades a demonstrar:**
- Página Home com métricas gerais
- Fase 1: Dados meteorológicos atualizados
- Fase 3: Simulação de sensores em tempo real
- Fase 4: Gráficos e previsões ML
- Fase 6: Upload e detecção YOLO

### 4. Sistema de Alertas AWS (2 minutos)
- Mostrar prints da configuração AWS
- Demonstrar envio de alerta via dashboard
- Mostrar e-mail e SMS recebidos

**Prints AWS a mostrar:**
- SNS topic
- SES verified identities
- Lambda function
- CloudWatch logs

### 5. Integração das Fases (2 minutos)
- Mostrar dados fluindo entre módulos
- Banco de dados populado
- Resultados das análises

**Demonstrar:**
- Leitura de sensor → Salvar no BD → Trigger alerta
- Imagem YOLO → Detecção → Alerta de praga
- Dados meteorológicos → Previsão ML → Recomendação

### 6. Conclusão (1 minuto)
- Resumir conquistas
- Destacar tecnologias utilizadas
- Próximos passos possíveis
- Agradecimentos

**Script sugerido:**
"Consolidamos com sucesso todas as fases em um sistema integrado e 
escalável. Utilizamos Python, AWS, IoT, ML e visão computacional. 
Como próximos passos, poderíamos expandir para mais culturas e 
implementar mobile app. Obrigado!"
```

### 7.2. Preparar Ambiente para Gravação

**Checklist pré-gravação:**
- [ ] Reiniciar computador (limpar memória)
- [ ] Fechar aplicações desnecessárias
- [ ] Testar microfone e áudio
- [ ] Preparar dados de demonstração no BD
- [ ] Ter imagens prontas para YOLO
- [ ] Configurar AWS com alertas funcionando
- [ ] Testar todos os botões da dashboard
- [ ] Preparar navegador com prints AWS abertos
- [ ] Definir quem será o narrador principal
- [ ] Ensaiar uma vez antes da gravação final

### 7.3. Gravação

**Ferramentas recomendadas:**
- **OBS Studio** (gratuito, open-source)
- **Loom** (fácil de usar, limite de 5min gratuito)
- **Zoom** (gravar reunião solo)
- **Camtasia** (pago, profissional)

**Configurações de gravação:**
- Resolução: 1080p (1920x1080)
- FPS: 30
- Áudio: 44.1kHz ou 48kHz
- Formato: MP4 (H.264)

### 7.4. Edição e Upload

**Edição básica:**
- [ ] Remover pausas longas
- [ ] Adicionar transições suaves
- [ ] Inserir títulos/legendas (opcional)
- [ ] Verificar sincronização áudio/vídeo
- [ ] Adicionar música de fundo (baixo volume)

**Upload no YouTube:**
1. Criar conta YouTube (se não tiver)
2. Upload do vídeo
3. Configurações:
   - Visibilidade: **Não listado**
   - Título: "FIAP Fase 7 - Sistema de Gestão para Agronegócio - Grupo [Nome]"
   - Descrição: Link do GitHub + resumo do projeto
   - Tags: FIAP, agronegócio, Python, AWS, IoT, ML, YOLO
4. Copiar link
5. Adicionar ao README.md do GitHub

---

## ✅ Fase 8: Revisão Final e Entrega

### 8.1. Checklist de Qualidade

**Código:**
- [ ] Todos os scripts executam sem erros
- [ ] Dependências estão no requirements.txt
- [ ] Variáveis sensíveis estão em .env (não commitadas)
- [ ] Código está comentado adequadamente
- [ ] README.md de cada fase está completo

**Dashboard:**
- [ ] Todos os botões funcionam
- [ ] Gráficos carregam corretamente
- [ ] Não há erros no console
- [ ] Interface é intuitiva e profissional

**AWS:**
- [ ] SNS está configurado e testado
- [ ] SES está configurado e testado
- [ ] Lambda está funcionando
- [ ] Prints estão salvos em docs/

**Documentação:**
- [ ] README.md principal está completo
- [ ] roadmap.md está detalhado
- [ ] docs/ contém todos os screenshots
- [ ] Instruções de instalação são claras
- [ ] Link do vídeo está no README

**Vídeo:**
- [ ] Duração <= 10 minutos
- [ ] Áudio está claro
- [ ] Demonstra todas as funcionalidades
- [ ] Está no YouTube como "não listado"
- [ ] Link está no README

### 8.2. Teste Final Completo

```bash
# 1. Clone em ambiente limpo
cd /tmp
git clone https://github.com/[SEU_USUARIO]/fiap_fase7_cap1.git
cd fiap_fase7_cap1

# 2. Configure ambiente
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure .env
cp .env.example .env
# Editar .env com credenciais reais

# 4. Setup database
python scripts/setup_database.py
python scripts/seed_data.py

# 5. Teste dashboard
cd dashboard
streamlit run app.py
# Testar todas as páginas e botões

# 6. Teste alertas
cd ../aws_alerts
python send_test_alert.py
# Verificar recebimento de e-mail e SMS
```

### 8.3. Preparar Entrega

**GitHub:**
- [ ] Fazer commit final
- [ ] Push para branch main
- [ ] Verificar que está público (ou adicionar @leoruiz197 se privado)
- [ ] Verificar que .env não foi commitado
- [ ] Verificar que arquivos grandes estão no .gitignore

**Documentos:**
- [ ] Criar PDF com link do GitHub
- [ ] Incluir nomes de todos os integrantes
- [ ] Incluir link do vídeo
- [ ] Incluir resumo do projeto (1 parágrafo)

**Portal FIAP:**
- [ ] Fazer upload do PDF
- [ ] Verificar prazo de entrega
- [ ] Não fazer commits após o prazo

### 8.4. Comunicação com Tutor

Se optar por repositório privado:

```markdown
Assunto: FIAP Fase 7 - Repositório Privado - Grupo [Nome]

Olá Professor,

Segue o link do nosso repositório da Fase 7:
https://github.com/[USUARIO]/fiap_fase7_cap1

O repositório está privado e adicionamos você (@leoruiz197) como colaborador.

Link do vídeo: [URL do YouTube]

Integrantes:
- [Nome 1]
- [Nome 2]
- [...]

Atenciosamente,
Grupo [Nome]
```

---

## 📊 Matriz de Responsabilidades Sugerida

Para grupos de até 5 pessoas:

| Responsabilidade | Membro 1 | Membro 2 | Membro 3 | Membro 4 | Membro 5 |
|------------------|----------|----------|----------|----------|----------|
| Fase 1: Migração e teste | ✓ | - | - | - | - |
| Fase 2: BD e modelos | - | ✓ | - | - | - |
| Fase 3: IoT e API | - | - | ✓ | - | - |
| Fase 4: ML e análises | ✓ | - | - | - | - |
| Fase 5: Infra AWS | - | - | - | ✓ | - |
| Fase 6: Visão YOLO | - | ✓ | - | - | - |
| Dashboard principal | - | - | ✓ | - | ✓ |
| Sistema de alertas AWS | - | - | - | ✓ | - |
| Documentação e README | ✓ | - | - | - | ✓ |
| Vídeo de apresentação | Todos | Todos | Todos | Todos | Todos |

**Para grupos menores:** distribuir as responsabilidades de forma equilibrada.

---

## 🛠️ Troubleshooting

### Problemas Comuns e Soluções

**1. Erro de importação entre fases**
```python
# Solução: Adicionar ao sys.path
import sys
sys.path.append('../phase2')
from orm.models import Sensor
```

**2. AWS credenciais não encontradas**
```bash
# Solução: Configurar AWS CLI
aws configure
# Ou adicionar ao .env
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

**3. Porta 8501 em uso (Streamlit)**
```bash
# Solução: Usar porta diferente
streamlit run app.py --server.port 8502
```

**4. PostgreSQL connection refused**
```bash
# Verificar se está rodando
sudo systemctl status postgresql
sudo systemctl start postgresql

# Ou usar SQLite para desenvolvimento
DATABASE_URL=sqlite:///./agronegocio.db
```

**5. ModuleNotFoundError: No module named 'streamlit'**
```bash
# Verificar se está no venv correto
which python
# Reinstalar dependências
pip install -r requirements.txt
```

---

## 📌 Recursos Adicionais

### Links Úteis

**Documentação Oficial:**
- [Streamlit Docs](https://docs.streamlit.io/)
- [AWS SNS](https://docs.aws.amazon.com/sns/)
- [AWS SES](https://docs.aws.amazon.com/ses/)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [YOLOv8](https://docs.ultralytics.com/)

**Tutoriais:**
- [Streamlit Multi-page Apps](https://docs.streamlit.io/library/get-started/multipage-apps)
- [AWS Lambda com Python](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)
- [ESP32 com MicroPython](https://docs.micropython.org/en/latest/esp32/quickref.html)

**Comunidades:**
- [Stack Overflow](https://stackoverflow.com/)
- [AWS Forums](https://repost.aws/)
- [Streamlit Community](https://discuss.streamlit.io/)

---

## 🎓 Critérios de Avaliação (Esperados)

### Funcionalidade (40%)
- ✅ Integração completa das Fases 1-6
- ✅ Dashboard funcional com todos os botões
- ✅ Sistema de alertas AWS operacional
- ✅ Demonstração de fluxo completo

### Qualidade do Código (20%)
- ✅ Organização e estrutura de pastas
- ✅ Código limpo e comentado
- ✅ Boas práticas de programação
- ✅ Tratamento de erros

### Documentação (20%)
- ✅ README.md completo e claro
- ✅ Roadmap detalhado
- ✅ Screenshots AWS adequados
- ✅ Instruções de instalação funcionais

### Apresentação em Vídeo (20%)
- ✅ Clareza na apresentação
- ✅ Demonstração de todas as funcionalidades
- ✅ Duração adequada (≤ 10 min)
- ✅ Qualidade de áudio/vídeo

---

## 📝 Notas Finais

### Dicas para Sucesso

1. **Comece cedo:** Não deixe para a última semana
2. **Teste frequentemente:** Valide cada integração antes de prosseguir
3. **Documente conforme desenvolve:** Não deixe documentação para o final
4. **Use controle de versão:** Commits frequentes e mensagens descritivas
5. **Peça ajuda:** Use o tutor, fóruns e comunidades
6. **Mantenha backup:** Use GitHub e backup local
7. **Seja realista:** Se algo não funcionar, documente e explique

### O que Fazer se Algo Falhar

**Se não conseguir implementar algo:**
1. Documente o que tentou
2. Explique o problema encontrado
3. Mostre o código/tentativa
4. Sugira solução alternativa
5. Não deixe código quebrado no main

**Exemplo de documentação de falha:**
```markdown
## Limitações Conhecidas

### Sistema de Alertas SMS
**Status:** Parcialmente implementado

**Problema:** Não foi possível obter aprovação da AWS para saída do 
sandbox do SES dentro do prazo do projeto. 

**Implementação atual:** Sistema funciona para e-mails verificados 
individualmente.

**Próximos passos:** Solicitar produção access no SES e adicionar 
validação de domínio.

**Código:** Implementação completa disponível em `aws_alerts/`, 
testado em ambiente sandbox.
```

---

## ✨ Conclusão

Este roadmap fornece um caminho completo para a consolidação do projeto da Fase 7. Adapte conforme necessário para o contexto e recursos do seu grupo.

**Boa sorte! 🚀**

---

**Última Atualização:** Novembro 2024  
**Versão do Roadmap:** 1.0.0  
**Autor:** Fase 7 - FIAP
