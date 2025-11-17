# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="docs/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Projeto: Sistema Agrícola Unificado - FarmTech Solutions
## Consolidação das Fases 1-6 + Sistema de Alertas AWS

## Atividade em Grupo: FIAP - 1TIAOB - 2025/1 - Fase 7 Cap 1

## 👨‍🎓 Integrantes: 
- <a href="">Alice C. M. Assis - RM 566233</a>
- <a href="">Leonardo S. Souza - RM 563928</a>
- <a href="">Lucas B. Francelino - RM 561409</a> 
- <a href="">Pedro L. T. Silva - RM 561644</a> 
- <a href="">Vitor A. Bezerra - RM 563001</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="proflucas.moreira@fiap.com.br">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="profandre.chiovato@fiap.com.br">André Godoi Chiovato</a>

---

## 📜 Descrição

Este repositório contém a **consolidação integrada de todas as fases** do projeto FarmTech Solutions, unificando em uma única estrutura Python os seguintes módulos:

- **Fase 1** – Cálculos Agrícolas + API Meteorológica + Análise em R
- **Fase 2** – Banco de Dados Relacional (MER/DER)
- **Fase 3** – IoT (ESP32, sensores e irrigação automática)
- **Fase 4** – Dashboard (Streamlit) + Machine Learning
- **Fase 5** – Cloud (AWS) + Segurança + Sistema de Alertas
- **Fase 6** – Visão Computacional (YOLO)
- **Fase 7** – Consolidação e Orquestração

### 🎯 Objetivo Principal

Criar um **sistema unificado** onde todas as funcionalidades das fases anteriores sejam acessíveis através de:
- **Dashboard principal** baseado em Streamlit (herdado da Fase 4)
- **Botões e comandos** para disparar cada serviço individualmente
- **Sistema de alertas AWS** (SNS/SES) que recebe eventos das Fases 1, 3 e 6
- **Integração de dados** entre todos os módulos através de banco de dados centralizado

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                  Dashboard Principal (Fase 4)               │
│                        Streamlit UI                          │
└─────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Fase 1     │    │   Fase 3     │    │   Fase 6     │
│  Cálculos    │    │   IoT        │    │   YOLO       │
│  Agrícolas   │    │   Sensores   │    │   Detecção   │
└──────────────┘    └──────────────┘    └──────────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              ▼
                    ┌──────────────────┐
                    │  Sistema AWS     │
                    │  Alertas         │
                    │  (SNS/SES)       │
                    └──────────────────┘
                              ▼
                    ┌──────────────────┐
                    │  Banco de Dados  │
                    │  (Fase 2)        │
                    └──────────────────┘
```

---

## 📦 Estrutura do Projeto

```
fiap_fase7_cap1/
├── README.md                          # Este arquivo
├── roadmap.md                         # Plano de integração detalhado
├── requirements.txt                   # Dependências consolidadas
├── .env.example                       # Exemplo de configuração
├── .gitignore                         # Arquivos ignorados
│
├── src/                               # Código fonte consolidado
│   ├── __init__.py
│   │
│   ├── fase1/                         # Cálculos agrícolas + API Clima
│   │   ├── __init__.py
│   │   ├── agro_calculations.py       # Cálculo de área, insumos
│   │   ├── weather_api.py             # Integração API meteorológica
│   │   └── r_analysis/                # Scripts R (opcional)
│   │
│   ├── fase2/                         # Banco de Dados
│   │   ├── __init__.py
│   │   ├── models.py                  # SQLAlchemy models (MER/DER)
│   │   ├── db.py                      # Engine, session, migrations
│   │   └── migrations/                # Scripts de migração
│   │
│   ├── fase3/                         # IoT e Sensores
│   │   ├── __init__.py
│   │   ├── api.py                     # FastAPI endpoints para ESP32
│   │   ├── iot_handlers.py            # CRUD sensores + automação bomba
│   │   └── esp32_examples/            # Código Arduino/ESP32
│   │
│   ├── fase4/                         # Dashboard + ML
│   │   ├── __init__.py
│   │   ├── streamlit_app.py           # Dashboard principal integrado
│   │   └── ml/                        # Modelos preditivos
│   │       ├── train.py
│   │       ├── predict.py
│   │       └── models/
│   │
│   ├── fase5/                         # AWS + Alertas
│   │   ├── __init__.py
│   │   └── aws/
│   │       ├── __init__.py
│   │       ├── alert_service.py       # SNS/SES integration
│   │       ├── iam_policy.md          # Políticas IAM necessárias
│   │       └── infra_notes.md         # Notas de infraestrutura
│   │
│   ├── fase6/                         # Visão Computacional
│   │   ├── __init__.py
│   │   ├── yolo_infer.py              # Detecção YOLO
│   │   └── camera/                    # ESP32-CAM examples
│   │
│   └── fase7/                         # Orquestração
│       ├── __init__.py
│       ├── launcher.py                # CLI para disparar fases
│       └── orchestrator.py            # Lógica de integração
│
├── docs/                              # Documentação
│   ├── aws_screenshots/               # Prints AWS (SNS/SES)
│   ├── architecture.png               # Diagrama de arquitetura
│   └── logo-fiap.png
│
├── tests/                             # Testes automatizados
│   └── ...
│
├── fiap_fase1_cap1-main/              # Repositórios originais (referência)
├── fiap_fase2_cap1-master/
├── fiap_fase3_cap1-novo-main/
├── fiap_fase4_cap1-main/
├── fiap_fase5_cap1-main/
└── fiap_fase6_cap1-main/
```

---

## 🚀 Como Executar

### 1️⃣ Pré-requisitos

- **Python 3.11+** (recomendado 3.13.2)
- **Git** instalado
- **Conta AWS** (para serviço de alertas)
- **Banco de dados** Oracle ou SQLite

### 2️⃣ Instalação

```bash
# Clone o repositório
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3️⃣ Configuração

Copie o arquivo de exemplo e configure as variáveis de ambiente:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:

```env
# Banco de Dados
SQL_LITE=true                          # true para SQLite, false para Oracle
DATABASE_URL=sqlite:///data/agro.db    # ou conexão Oracle
ORACLE_DSN=oracle.fiap.com.br:1521/ORCL
ORACLE_USER=seu_usuario
ORACLE_PASSWORD=sua_senha

# AWS
AWS_ACCESS_KEY_ID=sua_access_key
AWS_SECRET_ACCESS_KEY=sua_secret_key
AWS_REGION=us-east-1
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789:farm-alerts

# Aplicação
LOGGING_ENABLED=true
ENABLE_API=true                        # API para ESP32
API_PORT=8180
```

### 4️⃣ Migração do Banco de Dados

```bash
# Execute as migrações (cria tabelas)
python -m src.fase2.db migrate
```

### 5️⃣ Iniciar o Sistema

#### Opção A: Dashboard Completo (Recomendado)

```bash
# Inicia o dashboard principal com todas as integrações
streamlit run src/fase4/streamlit_app.py
```

Acesse no navegador: `http://localhost:8501`

#### Opção B: API de Sensores (IoT)

```bash
# Inicia apenas a API para receber dados do ESP32
uvicorn src.fase3.api:app --reload --port 8180
```

#### Opção C: Launcher via CLI

```bash
# Executa fases individuais via linha de comando
python -m src.fase7.launcher --fase 1  # Cálculos agrícolas
python -m src.fase7.launcher --fase 3  # IoT loop
python -m src.fase7.launcher --fase 6  # YOLO inference
```

---

## 🎛️ Funcionalidades do Dashboard

O dashboard principal (Fase 4) foi estendido para incluir:

### Menu Principal
- **🏠 Home** - Visão geral do sistema
- **🌾 Fase 1** - Cálculos agrícolas e previsão do tempo
- **💾 Fase 2** - Gerenciamento do banco de dados (CRUD)
- **🔌 Fase 3** - Monitoramento de sensores IoT e irrigação
- **📊 Fase 4** - Visualizações e ML preditivo
- **☁️ Fase 5** - Status AWS e envio de alertas
- **👁️ Fase 6** - Detecção de pragas/doenças (YOLO)
- **🔧 Fase 7** - Orquestração e logs do sistema

### Botões de Ação
Cada fase possui botões para:
- ▶️ **Iniciar** - Dispara o serviço da fase
- ⏸️ **Pausar** - Pausa execução (quando aplicável)
- 📈 **Ver Métricas** - Exibe resultados e visualizações
- 🔔 **Enviar Alerta** - Testa o sistema de notificações AWS

---

## 🚨 Sistema de Alertas AWS

### Descrição

O sistema de alertas utiliza **AWS SNS (Simple Notification Service)** ou **AWS SES (Simple Email Service)** para enviar notificações em tempo real quando:

- **Fase 1**: Condições climáticas adversas detectadas (geada, seca, tempestade)
- **Fase 3**: Sensores indicam valores críticos (umidade baixa, pH fora do ideal)
- **Fase 6**: Visão computacional detecta pragas ou doenças nas plantas

### Configuração AWS

#### 1. Criar Tópico SNS

```bash
# Via AWS CLI
aws sns create-topic --name farm-alerts --region us-east-1

# Anotar o ARN retornado (ex: arn:aws:sns:us-east-1:123456789:farm-alerts)
```

#### 2. Adicionar Assinantes

```bash
# Email
aws sns subscribe --topic-arn arn:aws:sns:us-east-1:123456789:farm-alerts \
    --protocol email --notification-endpoint seu-email@example.com

# SMS (requer verificação)
aws sns subscribe --topic-arn arn:aws:sns:us-east-1:123456789:farm-alerts \
    --protocol sms --notification-endpoint +5511999999999
```

#### 3. Política IAM Necessária

O usuário IAM precisa da seguinte política (ver `src/fase5/aws/iam_policy.md`):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish",
        "sns:Subscribe",
        "sns:ListTopics"
      ],
      "Resource": "arn:aws:sns:us-east-1:123456789:farm-alerts"
    }
  ]
}
```

### Exemplo de Uso

```python
from src.fase5.aws.alert_service import publish_alert

# Enviar alerta de umidade baixa
publish_alert(
    topic_arn="arn:aws:sns:us-east-1:123456789:farm-alerts",
    subject="⚠️ Alerta: Umidade Crítica no Campo 3",
    message="Sensor detectou umidade de 25% (abaixo do limite de 30%). Irrigação recomendada."
)
```

### Screenshots AWS

![SNS Topic](docs/aws_screenshots/sns_topic.png)
![SNS Subscription](docs/aws_screenshots/sns_subscription.png)
![Email Recebido](docs/aws_screenshots/email_alert.png)

---

## 🔗 Integração Entre Fases

### Fluxo de Dados

```
ESP32 Sensores (Fase 3)
    │
    ├──> API FastAPI (Fase 3)
    │         │
    │         ├──> Banco de Dados (Fase 2)
    │         │
    │         └──> Verifica Thresholds
    │                   │
    │                   └──> Alerta AWS (Fase 5) ← Email/SMS
    │
    └──> Dashboard (Fase 4)
              │
              ├──> Visualizações
              ├──> ML Preditivo (Fase 4)
              └──> Detecção YOLO (Fase 6)
                        │
                        └──> Se praga detectada → Alerta AWS
```

### Exemplos de Integração

#### 1. Sensor IoT → Banco → Dashboard

```python
# Fase 3: ESP32 envia leitura via POST
POST /api/sensor/reading
{
  "sensor_id": "DHT22-001",
  "temperatura": 28.5,
  "umidade": 62.3,
  "timestamp": "2025-11-17T14:00:00Z"
}

# Fase 2: Dados salvos no DB
INSERT INTO leitura_sensor (sensor_id, valor, data_leitura) VALUES (...)

# Fase 4: Dashboard atualiza gráfico em tempo real
```

#### 2. Clima Adverso → Alerta

```python
# Fase 1: API Meteorológica detecta geada
weather_data = get_weather("Campinas,SP")
if weather_data["temperatura"] < 5:
    # Fase 5: Envia alerta
    publish_alert(
        subject="❄️ Alerta: Risco de Geada",
        message="Temperatura prevista: 3°C. Proteger plantio."
    )
```

#### 3. YOLO Detecta Praga → Alerta

```python
# Fase 6: Detecta praga em imagem
detections = yolo_infer.detect("campo_3.jpg")
if "praga" in detections:
    # Fase 5: Alerta AWS
    publish_alert(
        subject="🐛 Alerta: Praga Detectada no Campo 3",
        message=f"Detecção: {detections['praga']} - Ação imediata necessária."
    )
```

---

## 📊 Tecnologias Utilizadas

### Backend
- **Python 3.13.2**
- **FastAPI** - API REST para IoT
- **SQLAlchemy** - ORM para banco de dados
- **oracledb** - Driver Oracle
- **boto3** - SDK AWS

### Frontend
- **Streamlit** - Dashboard interativo
- **Plotly** - Gráficos dinâmicos
- **Matplotlib/Seaborn** - Visualizações estáticas

### Machine Learning
- **scikit-learn** - Modelos preditivos
- **PyCaret** - AutoML
- **ultralytics (YOLO)** - Detecção de objetos

### IoT
- **ESP32** - Microcontrolador
- **DHT22** - Sensor temperatura/umidade
- **LDR** - Sensor pH (simulado)

### Cloud
- **AWS SNS** - Notificações push
- **AWS SES** - Email transacional
- **AWS EC2/ECS** - Deploy (opcional)

---

## 🧪 Testes

```bash
# Executar todos os testes
pytest tests/

# Testar módulo específico
pytest tests/test_fase3_api.py

# Com cobertura
pytest --cov=src tests/
```

---

## 📝 Dependências Principais

```txt
# Web Framework
streamlit==1.44.1
fastapi==0.115.12
uvicorn==0.34.3

# Banco de Dados
oracledb==3.1.0
SQLAlchemy==2.0.40

# Data Science
pandas==2.2.3
numpy==1.26.0
matplotlib==3.10.1
seaborn==0.13.2
scikit-learn==1.7.0
pycaret==3.0.0

# Computer Vision
ultralytics==8.0.0
opencv-python==4.8.0

# AWS
boto3==1.34.0

# Utils
python-dotenv==1.0.0
requests==2.31.0
```

Instalação completa: `pip install -r requirements.txt`

---

## 🗂️ Histórico de Versões

* **0.7.0** - 17/11/2025
    * Consolidação completa das Fases 1-6
    * Sistema de alertas AWS implementado
    * Dashboard unificado funcional
    * Documentação completa

* **0.6.0** - Fase 6 - Visão Computacional (YOLO)
* **0.5.0** - Fase 5 - AWS + Machine Learning
* **0.4.0** - Fase 4 - Dashboard Streamlit + ML
* **0.3.0** - Fase 3 - IoT ESP32 + Sensores
* **0.2.0** - Fase 2 - Banco de Dados MER/DER
* **0.1.0** - Fase 1 - Cálculos Agrícolas + API Clima

---

## 🤝 Contribuindo

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📧 Contato

Para dúvidas ou suporte:
- **Email**: contato@farmtechsolutions.com.br
- **Issues**: [GitHub Issues](https://github.com/Hinten/fiap_fase7_cap1/issues)

---

## 📄 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
<a property="dct:title" rel="cc:attributionURL" href="https://github.com/Hinten/fiap_fase7_cap1">Sistema Agrícola Unificado - FarmTech Solutions</a> por 
<a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre 
<a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.
</p>

---

## 🙏 Agradecimentos

- Prof. Lucas Gomes Moreira - Tutoria e suporte técnico
- Prof. André Godoi Chiovato - Coordenação do projeto
- FIAP - Infraestrutura e recursos
- Comunidade Open Source - Bibliotecas e ferramentas utilizadas

---

<p align="center">
Desenvolvido com ❤️ por Grupo 28 - FIAP 2025
</p>
