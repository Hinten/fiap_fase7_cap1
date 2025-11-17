# Notas de Infraestrutura AWS - FarmTech Solutions

## Visão Geral da Arquitetura Cloud

Este documento descreve a infraestrutura AWS recomendada para o deploy em produção do sistema FarmTech Solutions.

---

## Serviços AWS Utilizados

### 1. **SNS (Simple Notification Service)** ⭐ IMPLEMENTADO
- **Uso:** Sistema de alertas (email/SMS)
- **Configuração:**
  - Tópico: `farm-alerts`
  - Protocolos: Email, SMS
  - Região: us-east-1
- **Custo estimado:** ~$0.50/mês (dentro do free tier para uso moderado)

### 2. **EC2 (Elastic Compute Cloud)** - RECOMENDADO
- **Uso:** Hospedar dashboard e APIs
- **Instância recomendada:**
  - Tipo: `t3.small` (2 vCPU, 2 GB RAM)
  - SO: Ubuntu 22.04 LTS
  - Storage: 50 GB GP3
- **Custo estimado:** ~$15/mês
- **Alternativa:** t3.micro (1 vCPU, 1 GB) - ~$7.50/mês

### 3. **RDS (Relational Database Service)** - OPCIONAL
- **Uso:** Banco de dados gerenciado (alternativa ao Oracle FIAP)
- **Configuração recomendada:**
  - Engine: PostgreSQL 15
  - Instância: db.t3.micro
  - Storage: 20 GB
- **Custo estimado:** ~$15/mês
- **Alternativa:** Continuar usando banco Oracle FIAP (custo zero)

### 4. **S3 (Simple Storage Service)** - RECOMENDADO
- **Uso:** Armazenamento de imagens para YOLO, backups, logs
- **Configuração:**
  - Bucket: `farmtech-data`
  - Lifecycle: Mover para Glacier após 90 dias
- **Custo estimado:** ~$1-5/mês

### 5. **Lambda** - OPCIONAL (Arquitetura Serverless)
- **Uso:** Executar funções sob demanda (processamento YOLO, alertas)
- **Vantagem:** Custo muito baixo, escalabilidade automática
- **Custo estimado:** ~$0-2/mês

### 6. **ECS (Elastic Container Service)** - ALTERNATIVA
- **Uso:** Deploy com Docker containers
- **Configuração:**
  - Fargate (serverless) ou EC2
  - Task definitions para cada serviço
- **Custo estimado:** Variável, similar a EC2

---

## Opções de Deploy

### Opção 1: EC2 Tradicional (MAIS SIMPLES)

**Arquitetura:**
```
Internet → EC2 (t3.small)
           ├── Streamlit Dashboard (porta 8501)
           ├── FastAPI (porta 8180)
           ├── YOLO Inference
           └── SQLite local ou RDS PostgreSQL
```

**Passos:**
1. Criar instância EC2 Ubuntu 22.04
2. Instalar Python 3.11, pip, requirements
3. Clonar repositório
4. Configurar .env com credenciais
5. Iniciar serviços com systemd
6. Configurar Security Group (portas 8501, 8180, 22)

**Vantagens:**
- Simples de configurar
- Baixo custo
- Fácil debug

**Desvantagens:**
- Escalabilidade limitada
- Gerenciamento manual de updates

---

### Opção 2: Docker + ECS Fargate (ESCALÁVEL)

**Arquitetura:**
```
Internet → ALB (Load Balancer)
           ├── ECS Task: Dashboard
           ├── ECS Task: IoT API
           └── ECS Task: YOLO Worker
           
RDS PostgreSQL (backup automático)
S3 (imagens, modelos)
SNS (alertas)
```

**Passos:**
1. Criar Dockerfiles para cada serviço
2. Push para ECR (Elastic Container Registry)
3. Criar Task Definitions
4. Configurar Application Load Balancer
5. Deploy via ECS Fargate
6. Configurar Auto Scaling

**Vantagens:**
- Alta disponibilidade
- Auto-scaling
- Gerenciamento de containers

**Desvantagens:**
- Mais complexo
- Custo maior (~$30-50/mês)

---

### Opção 3: Serverless (Lambda + API Gateway)

**Arquitetura:**
```
Internet → API Gateway
           ├── Lambda: IoT Endpoint
           ├── Lambda: YOLO Inference
           └── Lambda: Weather Check
           
S3 (frontend estático)
DynamoDB ou RDS (dados)
SNS (alertas)
```

**Vantagens:**
- Custo muito baixo (pay-per-use)
- Escalabilidade infinita
- Zero gerenciamento de servidores

**Desvantagens:**
- Cold start (latência inicial)
- Limite de 15min por execução Lambda
- Dashboard precisa adaptação (não pode ser Streamlit tradicional)

---

## Exemplo: Deploy EC2 com Systemd

### 1. Criar Instância EC2

```bash
# Via AWS CLI
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.small \
  --key-name farmtech-key \
  --security-group-ids sg-0123456789abcdef \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=FarmTech-Server}]'
```

### 2. Conectar e Configurar

```bash
# SSH na instância
ssh -i farmtech-key.pem ubuntu@<EC2_PUBLIC_IP>

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python 3.11
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.11 python3.11-venv python3-pip -y

# Clonar repositório
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1

# Criar ambiente virtual
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configurar .env
cp .env.example .env
nano .env  # Editar credenciais
```

### 3. Criar Serviços Systemd

#### Dashboard Service (`/etc/systemd/system/farmtech-dashboard.service`)

```ini
[Unit]
Description=FarmTech Streamlit Dashboard
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/fiap_fase7_cap1
Environment="PATH=/home/ubuntu/fiap_fase7_cap1/venv/bin"
ExecStart=/home/ubuntu/fiap_fase7_cap1/venv/bin/streamlit run src/fase4/streamlit_app.py --server.port=8501 --server.address=0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

#### IoT API Service (`/etc/systemd/system/farmtech-api.service`)

```ini
[Unit]
Description=FarmTech IoT API
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/fiap_fase7_cap1
Environment="PATH=/home/ubuntu/fiap_fase7_cap1/venv/bin"
ExecStart=/home/ubuntu/fiap_fase7_cap1/venv/bin/uvicorn src.fase3.api:app --host 0.0.0.0 --port 8180
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Iniciar Serviços

```bash
sudo systemctl daemon-reload
sudo systemctl enable farmtech-dashboard
sudo systemctl enable farmtech-api
sudo systemctl start farmtech-dashboard
sudo systemctl start farmtech-api

# Verificar status
sudo systemctl status farmtech-dashboard
sudo systemctl status farmtech-api
```

### 4. Configurar Security Group

| Tipo | Protocolo | Porta | Origem | Descrição |
|------|-----------|-------|--------|-----------|
| SSH | TCP | 22 | Seu IP | Acesso SSH |
| Custom TCP | TCP | 8501 | 0.0.0.0/0 | Dashboard |
| Custom TCP | TCP | 8180 | 0.0.0.0/0 | API IoT |

### 5. Configurar Domínio (Opcional)

```bash
# Com Route53 ou outro DNS
# Apontar domínio para IP elástico da EC2

# Exemplo:
# dashboard.farmtech.com → 54.123.45.67:8501
# api.farmtech.com → 54.123.45.67:8180
```

---

## Segurança

### 1. IAM Roles (Em vez de access keys)

Para EC2, use IAM Instance Profile em vez de access keys hardcoded:

```bash
# Criar role
aws iam create-role --role-name FarmTech-EC2-Role \
  --assume-role-policy-document file://trust-policy.json

# Anexar política SNS
aws iam attach-role-policy \
  --role-name FarmTech-EC2-Role \
  --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess

# Criar instance profile
aws iam create-instance-profile --instance-profile-name FarmTech-EC2-Profile
aws iam add-role-to-instance-profile \
  --instance-profile-name FarmTech-EC2-Profile \
  --role-name FarmTech-EC2-Role

# Associar à instância EC2
aws ec2 associate-iam-instance-profile \
  --instance-id i-0123456789abcdef \
  --iam-instance-profile Name=FarmTech-EC2-Profile
```

Assim, não precisa de `AWS_ACCESS_KEY_ID` no `.env`!

### 2. Secrets Manager (Produção)

Em vez de `.env`, use AWS Secrets Manager:

```python
import boto3
import json

def get_secret():
    client = boto3.client('secretsmanager', region_name='us-east-1')
    response = client.get_secret_value(SecretId='farmtech/prod/credentials')
    return json.loads(response['SecretString'])

secrets = get_secret()
database_url = secrets['DATABASE_URL']
```

### 3. HTTPS com Certificado SSL

Use AWS Certificate Manager (ACM) + Application Load Balancer para HTTPS gratuito.

---

## Monitoramento

### CloudWatch

```bash
# Criar alarmes
aws cloudwatch put-metric-alarm \
  --alarm-name farmtech-cpu-high \
  --alarm-description "Alert when CPU exceeds 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-0123456789abcdef \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:us-east-1:123456789:farm-alerts
```

### Logs

```python
# Enviar logs para CloudWatch
import watchtower
import logging

logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler())
```

---

## Backup

### Snapshots EC2

```bash
# Criar snapshot diário do volume
aws ec2 create-snapshot \
  --volume-id vol-0123456789abcdef \
  --description "FarmTech Daily Backup"
```

### Backup RDS Automático

Habilitado por padrão, retenção de 7 dias.

### Backup Banco SQLite para S3

```bash
# Crontab diário
0 2 * * * /usr/bin/aws s3 cp /home/ubuntu/fiap_fase7_cap1/data/agro.db s3://farmtech-backups/daily/$(date +\%Y-\%m-\%d).db
```

---

## Custos Estimados (Mensal)

| Serviço | Configuração | Custo |
|---------|--------------|-------|
| EC2 t3.small | 2 vCPU, 2 GB RAM | $15.00 |
| EBS 50 GB | GP3 Storage | $4.00 |
| SNS | 1000 emails/mês | $0.00 (free tier) |
| S3 | 10 GB storage | $0.23 |
| Data Transfer | 10 GB out | $0.90 |
| **Total Mensal** | | **~$20.13** |

**Nota:** Valores aproximados para região us-east-1. Pode variar.

---

## Terraform (Infraestrutura como Código)

Para automatizar o deploy:

```hcl
# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "farmtech" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.small"
  key_name      = "farmtech-key"
  
  tags = {
    Name = "FarmTech-Server"
  }
}

resource "aws_sns_topic" "alerts" {
  name = "farm-alerts"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = "contato@farmtech.com"
}
```

Deploy:
```bash
terraform init
terraform plan
terraform apply
```

---

## Próximos Passos

1. ✅ Configurar SNS (já feito)
2. ⏳ Provisionar EC2 ou ECS
3. ⏳ Deploy da aplicação
4. ⏳ Configurar monitoramento
5. ⏳ Implementar backups
6. ⏳ Testar DR (Disaster Recovery)

---

**Última Atualização:** 17/11/2025  
**Responsável:** Grupo 28 - FIAP
