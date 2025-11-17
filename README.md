# Projeto Fase 7 — Consolidação do Sistema de Gestão para Agronegócio

## 📋 Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Executar](#como-executar)
- [Funcionalidades por Fase](#funcionalidades-por-fase)
- [Sistema de Mensageria AWS](#sistema-de-mensageria-aws)
- [Vídeo de Apresentação](#vídeo-de-apresentação)
- [Créditos e Referências](#créditos-e-referências)

---

## 🎯 Sobre o Projeto

Este projeto representa a **consolidação e integração** de todas as etapas desenvolvidas nas Fases 1 a 6 do programa FIAP, criando um **sistema completo de gestão para o agronegócio**. O sistema integra:

- **Análise de dados agrícolas** (cálculos, meteorologia)
- **Banco de dados estruturado** (MER/DER)
- **IoT e automação** (ESP32, sensores, irrigação inteligente)
- **Dashboard interativo** (Streamlit + Machine Learning)
- **Infraestrutura Cloud** (AWS, segurança)
- **Visão computacional** (YOLO para monitoramento visual)
- **Sistema de alertas** (Mensageria AWS com SNS/SES)

### Objetivo da Fase 7

Integrar todos os serviços desenvolvidos anteriormente em uma **única pasta de projeto Python** com:
- Dashboard unificada com botões para disparar cada serviço
- Sistema de alertas automatizados via e-mail/SMS
- Arquitetura escalável e segura hospedada na AWS
- Documentação completa e vídeo demonstrativo

---

## 📁 Estrutura do Repositório

```
fiap_fase7_cap1/
│
├── phase1/                      # Fase 1: Base de Dados Inicial
│   ├── calculos/               # Cálculos de área e manejo de insumos
│   ├── api_meteorologica/      # Integração com API meteorológica
│   ├── analise_estatistica/    # Análises em R
│   └── README.md
│
├── phase2/                      # Fase 2: Banco de Dados Estruturado
│   ├── modelos/                # MER e DER
│   ├── scripts_sql/            # Scripts de criação e migração
│   ├── orm/                    # Modelos SQLAlchemy
│   └── README.md
│
├── phase3/                      # Fase 3: IoT e Automação Inteligente
│   ├── firmware_esp32/         # Código para ESP32
│   ├── sensores/               # Simuladores e lógica de sensores
│   ├── api_crud/               # API REST para operações CRUD
│   └── README.md
│
├── phase4/                      # Fase 4: Dashboard Interativo com Data Science
│   ├── streamlit_app/          # Aplicação Streamlit original
│   ├── modelos_ml/             # Modelos de Machine Learning
│   ├── notebooks/              # Jupyter Notebooks para análise
│   └── README.md
│
├── phase5/                      # Fase 5: Cloud Computing & Segurança
│   ├── infraestrutura/         # Templates CloudFormation/Terraform
│   ├── scripts_deploy/         # Scripts de deploy AWS
│   ├── seguranca/              # Documentação ISO 27001/27002
│   └── README.md
│
├── phase6/                      # Fase 6: Visão Computacional com YOLO
│   ├── modelo_yolo/            # Pesos e configuração do modelo
│   ├── inferencia/             # Scripts de inferência
│   ├── images/                 # Imagens estáticas para processamento
│   └── README.md
│
├── dashboard/                   # Dashboard Principal Unificada
│   ├── app.py                  # Aplicação Streamlit principal
│   ├── pages/                  # Páginas da dashboard
│   ├── components/             # Componentes reutilizáveis
│   ├── utils/                  # Funções auxiliares
│   └── README.md
│
├── aws_alerts/                  # Sistema de Mensageria AWS
│   ├── lambda_handler.py       # Função Lambda para alertas
│   ├── sns_config.py           # Configuração SNS
│   ├── ses_config.py           # Configuração SES (e-mail)
│   ├── templates/              # Templates de e-mail/SMS
│   └── README.md
│
├── scripts/                     # Scripts Utilitários
│   ├── setup_database.py       # Configuração inicial do BD
│   ├── run_phase1.sh           # Executar serviços Fase 1
│   ├── run_phase2.sh           # Executar serviços Fase 2
│   ├── run_phase3.sh           # Executar serviços Fase 3
│   ├── run_phase6.sh           # Executar serviços Fase 6
│   └── seed_data.py            # Popular banco com dados de exemplo
│
├── data/                        # Dados e Datasets
│   ├── samples/                # Amostras de dados
│   ├── images/                 # Imagens para visão computacional
│   └── exports/                # Exportações e relatórios
│
├── docs/                        # Documentação
│   ├── arquitetura.md          # Diagrama de arquitetura
│   ├── aws_screenshots/        # Prints das configurações AWS
│   ├── video_roteiro.md        # Roteiro do vídeo de apresentação
│   └── instalacao_detalhada.md # Guia detalhado de instalação
│
├── roadmap/                     # Planejamento
│   └── roadmap.md              # Roadmap completo do projeto
│
├── .env.example                 # Exemplo de variáveis de ambiente
├── .gitignore                   # Arquivos a serem ignorados
├── requirements.txt             # Dependências Python
├── docker-compose.yml           # Configuração Docker (opcional)
└── README.md                    # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

### Backend & Análise
- **Python 3.8+** - Linguagem principal
- **R** - Análise estatística (Fase 1)
- **PostgreSQL** - Banco de dados relacional
- **SQLAlchemy** - ORM para Python
- **FastAPI/Flask** - APIs REST

### Frontend & Visualização
- **Streamlit** - Dashboard interativa
- **Plotly** - Gráficos interativos
- **Matplotlib/Seaborn** - Visualizações estáticas

### Machine Learning & IA
- **Scikit-learn** - Modelos de ML
- **YOLO (YOLOv5/YOLOv8)** - Visão computacional
- **PyTorch/TensorFlow** - Deep Learning

### IoT & Hardware
- **ESP32** - Microcontrolador
- **DHT22** - Sensor de temperatura e umidade
- **LDR** - Sensor de luminosidade (proxy para pH)
- **MicroPython/Arduino** - Firmware

### Cloud & Infraestrutura
- **Amazon Web Services (AWS)**
  - EC2 - Hospedagem de aplicações
  - RDS - Banco de dados gerenciado
  - S3 - Armazenamento de objetos
  - SNS - Notificações via SMS
  - SES - Envio de e-mails
  - Lambda - Funções serverless
  - CloudWatch - Monitoramento
  - IAM - Gerenciamento de acesso

### DevOps & Ferramentas
- **Git/GitHub** - Controle de versão
- **Docker** - Containerização
- **VS Code** - IDE de desenvolvimento

---

## ✅ Pré-requisitos

### Software Necessário
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git
- PostgreSQL 12+ (ou SQLite para desenvolvimento local)
- R 4.0+ (para análises da Fase 1)
- Node.js (opcional, para ferramentas auxiliares)

### Contas e Credenciais
- Conta AWS (para serviços de mensageria e hospedagem)
- API Key para serviço meteorológico (OpenWeatherMap, WeatherAPI, etc.)
- E-mail verificado no Amazon SES (para envio de alertas)
- Número de telefone verificado no Amazon SNS (para SMS)

### Hardware (Opcional)
- ESP32 (para testes físicos de IoT)
- Sensores DHT22, LDR
- ESP32-CAM (para captura de imagens em tempo real)

---

## 📦 Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1
```

### 2. Criar Ambiente Virtual Python

```bash
python -m venv .venv

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Copie o arquivo de exemplo e edite com suas credenciais:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
# Banco de Dados
DATABASE_URL=postgresql://usuario:senha@localhost:5432/agronegocio
# ou para desenvolvimento local:
# DATABASE_URL=sqlite:///./agronegocio.db

# API Meteorológica
WEATHER_API_KEY=sua_chave_api_aqui
WEATHER_API_URL=https://api.openweathermap.org/data/2.5

# AWS Credentials
AWS_ACCESS_KEY_ID=sua_access_key
AWS_SECRET_ACCESS_KEY=sua_secret_key
AWS_REGION=us-east-1

# SNS (SMS)
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789012:alertas-fazenda

# SES (E-mail)
SES_SENDER_EMAIL=noreply@suafazenda.com.br
SES_RECIPIENT_EMAILS=gestor@suafazenda.com.br,operador@suafazenda.com.br

# ESP32 (se estiver usando hardware físico)
ESP32_IP_ADDRESS=192.168.1.100
ESP32_API_ENDPOINT=http://192.168.1.100/api

# YOLO Model
YOLO_MODEL_PATH=./phase6/modelo_yolo/best.pt
YOLO_CONFIDENCE_THRESHOLD=0.5
```

### 5. Configurar Banco de Dados

```bash
# Criar banco de dados
python scripts/setup_database.py

# Popular com dados de exemplo (opcional)
python scripts/seed_data.py
```

### 6. Instalar R e Pacotes (Para Fase 1)

```r
# No console R
install.packages(c("tidyverse", "ggplot2", "forecast", "lubridate"))
```

---

## 🚀 Como Executar

### Iniciar Dashboard Principal

A dashboard principal integra todas as funcionalidades e permite executar cada serviço:

```bash
cd dashboard
streamlit run app.py
```

Acesse no navegador: `http://localhost:8501`

### Executar Serviços Individualmente

#### Fase 1: Análise de Dados e Meteorologia
```bash
bash scripts/run_phase1.sh
# ou
python phase1/api_meteorologica/fetch_weather.py
```

#### Fase 2: Operações de Banco de Dados
```bash
bash scripts/run_phase2.sh
# ou
python phase2/scripts_sql/migrate.py
```

#### Fase 3: Simulador IoT
```bash
bash scripts/run_phase3.sh
# ou
python phase3/sensores/simulador.py
```

#### Fase 4: Dashboard Streamlit Original
```bash
cd phase4/streamlit_app
streamlit run app.py
```

#### Fase 6: Inferência YOLO
```bash
bash scripts/run_phase6.sh
# ou
python phase6/inferencia/detect.py --source ./data/images/
```

### Executar Sistema de Alertas AWS

```bash
# Configurar SNS/SES (necessário fazer apenas uma vez)
python aws_alerts/setup_aws.py

# Testar envio de alerta
python aws_alerts/send_test_alert.py
```

---

## 🔧 Funcionalidades por Fase

### Fase 1: Base de Dados Inicial
**Objetivo:** Estabelecer a base de dados com cálculos agrícolas e integração meteorológica.

**Funcionalidades:**
- ✅ Cálculo de área de plantio
- ✅ Gestão de insumos agrícolas
- ✅ Integração com API meteorológica pública
- ✅ Análise estatística de dados meteorológicos em R
- ✅ Histórico de condições climáticas

**Repositório Original:** [fiap_fase1_cap1](https://github.com/Hinten/fiap_fase1_cap1)

---

### Fase 2: Banco de Dados Estruturado
**Objetivo:** Estruturar banco de dados relacional completo.

**Funcionalidades:**
- ✅ Modelo Entidade-Relacionamento (MER)
- ✅ Diagrama Entidade-Relacionamento (DER)
- ✅ Scripts SQL de criação e migração
- ✅ Modelos ORM (SQLAlchemy)
- ✅ Integração com dados da Fase 1
- ✅ Consultas e relatórios

**Repositório Original:** [fiap_fase2_cap1](https://github.com/treino258/fiap_fase2_cap1)

---

### Fase 3: IoT e Automação Inteligente
**Objetivo:** Desenvolver sistema IoT com ESP32 para automação agrícola.

**Funcionalidades:**
- ✅ Leitura de sensores (DHT22 para umidade/temperatura, LDR para luminosidade)
- ✅ Lógica de acionamento automático de irrigação
- ✅ API REST para operações CRUD
- ✅ Integração com banco de dados (Fase 2)
- ✅ Dashboard de monitoramento em tempo real
- ✅ Alertas baseados em limiares de sensores

**Sensores Utilizados:**
- **DHT22:** Temperatura e umidade do solo
- **LDR:** Luminosidade (proxy para medição de pH)
- **Relé:** Acionamento de bomba de irrigação

**Repositório Original:** [fiap_fase3_cap1-novo](https://github.com/Hinten/fiap_fase3_cap1-novo)

---

### Fase 4: Dashboard Interativo com Data Science
**Objetivo:** Criar dashboard com ML para análise preditiva e tomada de decisão.

**Funcionalidades:**
- ✅ Dashboard Streamlit interativa
- ✅ Modelos de Machine Learning (Scikit-learn)
- ✅ Previsão de necessidades de irrigação
- ✅ Análise de tendências e padrões
- ✅ Visualizações interativas (Plotly, Matplotlib)
- ✅ Monitor físico (LCD + Serial Plotter no ESP32)
- ✅ Recomendações automatizadas de manejo

**Modelos ML Implementados:**
- Regressão Linear (previsão de consumo de água)
- Random Forest (classificação de necessidade de irrigação)
- K-Means (clustering de áreas similares)

**Repositório Original:** [fiap_fase4_cap1](https://github.com/Al1ce4-AI/fiap_fase4_cap1)

---

### Fase 5: Cloud Computing & Segurança
**Objetivo:** Hospedar infraestrutura na AWS com padrões de segurança.

**Funcionalidades:**
- ✅ Hospedagem em AWS (EC2, RDS, S3)
- ✅ Configuração de segurança (IAM, Security Groups)
- ✅ Aplicação de normas ISO 27001 e ISO 27002
- ✅ Backup automático de dados
- ✅ Monitoramento com CloudWatch
- ✅ Escalabilidade automática

**Serviços AWS Utilizados:**
- **EC2:** Hospedagem da aplicação
- **RDS PostgreSQL:** Banco de dados gerenciado
- **S3:** Armazenamento de imagens e arquivos
- **CloudWatch:** Logs e métricas
- **IAM:** Controle de acesso

**Repositório Original:** [fiap_fase5_cap1](https://github.com/Hinten/fiap_fase5_cap1)

---

### Fase 6: Visão Computacional com Redes Neurais
**Objetivo:** Implementar sistema de visão computacional para monitoramento de lavouras.

**Funcionalidades:**
- ✅ Modelo YOLO treinado para detecção de:
  - Pragas e insetos
  - Doenças em plantas
  - Crescimento irregular
  - Deficiências nutricionais
- ✅ Processamento de imagens estáticas
- ✅ Interface para upload de imagens
- ✅ Relatórios com detecções e recomendações
- ✅ Opção de integração com ESP32-CAM (tempo real)

**Repositório Original:** [fiap_fase6_cap1](https://github.com/Hinten/fiap_fase6_cap1)

---

## 📧 Sistema de Mensageria AWS

### Arquitetura de Alertas

O sistema de mensageria monitora em tempo real as condições da fazenda e envia alertas automatizados via **e-mail (SES)** e **SMS (SNS)**.

### Triggers de Alertas

#### 1. Alertas de Sensores (Fase 1 e 3)
- **Umidade baixa:** Umidade do solo < 30%
- **Temperatura alta:** Temperatura > 35°C
- **Luminosidade inadequada:** Fora do intervalo ideal
- **Falha de sensor:** Sensor não responde

#### 2. Alertas de Visão Computacional (Fase 6)
- **Praga detectada:** Confiança > 70%
- **Doença identificada:** Requer ação imediata
- **Crescimento anormal:** Padrão fora do esperado

#### 3. Alertas Preditivos (Fase 4)
- **Previsão de escassez hídrica:** ML prevê necessidade alta
- **Janela de plantio ideal:** Condições meteorológicas favoráveis

### Configuração do Sistema de Alertas

#### 1. Configurar Amazon SNS (SMS)

```bash
# Criar tópico SNS
aws sns create-topic --name alertas-fazenda

# Subscrever número de telefone
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:alertas-fazenda \
  --protocol sms \
  --notification-endpoint +5511999999999
```

#### 2. Configurar Amazon SES (E-mail)

```bash
# Verificar e-mail remetente
aws ses verify-email-identity --email-address noreply@suafazenda.com.br

# Verificar e-mail destinatário (modo sandbox)
aws ses verify-email-identity --email-address gestor@suafazenda.com.br
```

#### 3. Deploy da Função Lambda

```bash
cd aws_alerts
# Empacotar função Lambda
zip -r lambda_function.zip lambda_handler.py sns_config.py ses_config.py templates/

# Fazer upload para AWS
aws lambda create-function \
  --function-name ProcessarAlertasFazenda \
  --runtime python3.9 \
  --role arn:aws:iam::123456789012:role/lambda-execution-role \
  --handler lambda_handler.lambda_handler \
  --zip-file fileb://lambda_function.zip
```

#### 4. Configurar Trigger

A função Lambda pode ser acionada de várias formas:
- **API Gateway:** Endpoint HTTP para chamadas da dashboard
- **CloudWatch Events:** Execução periódica (cron)
- **DynamoDB Streams:** Trigger em inserções no BD
- **SNS:** Mensagens de outros serviços

### Exemplo de Template de Alerta

**E-mail:**
```
Assunto: 🚨 Alerta - Umidade Baixa Detectada

Olá,

Foi detectado um alerta crítico na sua fazenda:

📍 Localização: Setor A - Parcela 3
⏰ Horário: 2024-01-15 14:30:00
🌡️ Tipo: Umidade do Solo Baixa
📊 Valor Medido: 25% (limite mínimo: 30%)

🔧 Ação Recomendada:
- Ativar sistema de irrigação imediatamente
- Verificar funcionamento da bomba d'água
- Programar irrigação para as próximas 6 horas

Dashboard: https://dashboard.suafazenda.com.br
```

**SMS:**
```
⚠️ Fazenda: Umidade baixa (25%) - Setor A. Ação: ativar irrigação. Dashboard: https://bit.ly/fazenda
```

### Screenshots da Configuração AWS

Os prints detalhados da configuração estão disponíveis em:
- `docs/aws_screenshots/sns_configuration.png`
- `docs/aws_screenshots/ses_configuration.png`
- `docs/aws_screenshots/lambda_function.png`
- `docs/aws_screenshots/cloudwatch_logs.png`

---

## 🎥 Vídeo de Apresentação

### Link do Vídeo
📹 **[Apresentação Completa - Fase 7 (YouTube - Não Listado)]**

*[INSERIR LINK DO VÍDEO AQUI APÓS GRAVAÇÃO]*

### Roteiro do Vídeo (Máximo 10 minutos)

1. **Introdução (1 min)**
   - Apresentação do projeto e objetivos
   - Visão geral da arquitetura

2. **Estrutura do Repositório (1 min)**
   - Navegação pelas pastas
   - Organização do código

3. **Demonstração da Dashboard (3 min)**
   - Inicialização da aplicação
   - Navegação pelas funcionalidades
   - Execução de serviços via botões

4. **Sistema de Alertas (2 min)**
   - Configuração AWS (prints)
   - Demonstração de envio de alerta
   - E-mail e SMS recebidos

5. **Integração das Fases (2 min)**
   - Fase 1: Dados meteorológicos
   - Fase 3: Simulação IoT
   - Fase 6: Detecção YOLO

6. **Conclusão (1 min)**
   - Resultados alcançados
   - Próximos passos
   - Agradecimentos

---

## 👥 Créditos e Referências

### Repositórios Originais das Fases Anteriores

- **Fase 1:** [fiap_fase1_cap1](https://github.com/Hinten/fiap_fase1_cap1)
- **Fase 2:** [fiap_fase2_cap1](https://github.com/treino258/fiap_fase2_cap1)
- **Fase 3:** [fiap_fase3_cap1-novo](https://github.com/Hinten/fiap_fase3_cap1-novo)
- **Fase 4:** [fiap_fase4_cap1](https://github.com/Al1ce4-AI/fiap_fase4_cap1)
- **Fase 5:** [fiap_fase5_cap1](https://github.com/Hinten/fiap_fase5_cap1)
- **Fase 6:** [fiap_fase6_cap1](https://github.com/Hinten/fiap_fase6_cap1)

### Equipe do Projeto
*[INSERIR NOMES DOS INTEGRANTES DO GRUPO AQUI]*

### Instituição
**FIAP - Faculdade de Informática e Administração Paulista**  
Programa de Pós-Graduação - Fase 7

### Tutor
**GitHub:** [@leoruiz197](https://github.com/leoruiz197)

### Tecnologias e Ferramentas
- Python Software Foundation
- Streamlit
- Amazon Web Services (AWS)
- YOLOv5/YOLOv8 (Ultralytics)
- Scikit-learn
- PostgreSQL
- ESP32 (Espressif Systems)

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do programa FIAP.

---

## 📞 Contato

Para dúvidas ou sugestões sobre o projeto:
- **GitHub Issues:** [Criar Issue](https://github.com/Hinten/fiap_fase7_cap1/issues)
- **E-mail:** *[INSERIR E-MAIL DO GRUPO]*

---

**Última Atualização:** Novembro 2024  
**Versão:** 1.0.0
