# Sistema de Mensageria AWS - Alertas

## 📋 Descrição

Sistema de alertas automatizados via e-mail (SES) e SMS (SNS) integrado com AWS Lambda.

## 🎯 Funcionalidades

- Envio de e-mails via Amazon SES
- Envio de SMS via Amazon SNS
- Função Lambda para processamento de alertas
- Templates personalizáveis
- Triggers automáticos
- Integração com dashboard
- Histórico de alertas

## 📂 Estrutura

```
aws_alerts/
├── lambda_handler.py    # Função Lambda principal
├── sns_config.py        # Configuração SNS (SMS)
├── ses_config.py        # Configuração SES (E-mail)
├── templates/           # Templates de mensagens
│   ├── email_alerta.html
│   ├── sms_alerta.txt
│   └── email_relatorio.html
├── setup_aws.py         # Script de configuração inicial
├── send_test_alert.py   # Script para teste
└── README.md
```

## ☁️ Arquitetura AWS

```
┌─────────────┐
│  Dashboard  │
│  ou Sensor  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ API Gateway │ (opcional)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Lambda    │ ─── Processar alerta
└──────┬──────┘
       │
       ├──────────────┬──────────────┐
       ▼              ▼              ▼
   ┌─────┐        ┌─────┐       ┌──────┐
   │ SNS │        │ SES │       │  DB  │
   │(SMS)│        │(Email)│     │ (Log)│
   └─────┘        └─────┘       └──────┘
```

## 🚀 Setup AWS

### 1. Configurar Amazon SNS (SMS)

```bash
# Criar tópico
aws sns create-topic --name alertas-fazenda

# Output: arn:aws:sns:us-east-1:123456789012:alertas-fazenda

# Subscrever número
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:alertas-fazenda \
  --protocol sms \
  --notification-endpoint +5511999999999
```

### 2. Configurar Amazon SES (E-mail)

```bash
# Verificar e-mail remetente
aws ses verify-email-identity --email-address noreply@fazenda.com.br

# Verificar e-mail destinatário (sandbox)
aws ses verify-email-identity --email-address gestor@fazenda.com.br

# Criar template
aws ses create-template --cli-input-json file://templates/email_template.json
```

### 3. Criar Função Lambda

```bash
# Empacotar
zip -r lambda_function.zip lambda_handler.py sns_config.py ses_config.py

# Criar função
aws lambda create-function \
  --function-name ProcessarAlertasFazenda \
  --runtime python3.9 \
  --role arn:aws:iam::123456789012:role/lambda-execution-role \
  --handler lambda_handler.lambda_handler \
  --zip-file fileb://lambda_function.zip \
  --timeout 30 \
  --memory-size 256
```

### 4. Configurar Variáveis de Ambiente

```bash
aws lambda update-function-configuration \
  --function-name ProcessarAlertasFazenda \
  --environment Variables="{
    SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789012:alertas-fazenda,
    SES_SENDER_EMAIL=noreply@fazenda.com.br,
    SES_RECIPIENT_EMAILS=gestor@fazenda.com.br
  }"
```

### 5. Criar API Gateway (Opcional)

```bash
aws apigatewayv2 create-api \
  --name alertas-api \
  --protocol-type HTTP \
  --target arn:aws:lambda:us-east-1:123456789012:function:ProcessarAlertasFazenda
```

## 🔔 Tipos de Alertas

### 1. Alertas de Sensores (Fase 1/3)

```json
{
  "tipo": "Umidade Baixa",
  "mensagem": "Umidade do solo está em 25%, abaixo do limite de 30%",
  "severidade": "CRITICAL",
  "setor": "Setor A - Parcela 3",
  "valor": "25%",
  "limiar": "30%",
  "sensor_id": "DHT22-001",
  "timestamp": "2024-01-15T14:30:00"
}
```

### 2. Alertas de Visão Computacional (Fase 6)

```json
{
  "tipo": "Praga Detectada",
  "mensagem": "Lagarta detectada com 87% de confiança",
  "severidade": "CRITICAL",
  "setor": "Setor B - Parcela 1",
  "valor": "87%",
  "classe": "lagarta",
  "bbox": [120, 45, 180, 95],
  "imagem_url": "s3://fazenda-images/detecao_001.jpg",
  "timestamp": "2024-01-15T15:45:00"
}
```

### 3. Alertas Preditivos (Fase 4)

```json
{
  "tipo": "Previsão de Escassez Hídrica",
  "mensagem": "Modelo prevê necessidade alta de irrigação nas próximas 48h",
  "severidade": "WARNING",
  "setor": "Todos os setores",
  "valor": "85% probabilidade",
  "acao_sugerida": "Preparar sistema de irrigação",
  "timestamp": "2024-01-15T08:00:00"
}
```

## 📧 Templates de Mensagens

### E-mail

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        .header { background: #4CAF50; color: white; padding: 20px; }
        .content { padding: 20px; }
        .alert-critical { color: #d32f2f; font-weight: bold; }
        .alert-warning { color: #f57c00; }
        .alert-info { color: #1976d2; }
    </style>
</head>
<body>
    <div class="header">
        <h2>🚨 Alerta - Sistema de Gestão Fazenda</h2>
    </div>
    <div class="content">
        <p><strong>Tipo:</strong> {{tipo}}</p>
        <p><strong>Severidade:</strong> <span class="alert-{{severidade}}">{{severidade}}</span></p>
        <p><strong>Setor:</strong> {{setor}}</p>
        <p><strong>Mensagem:</strong> {{mensagem}}</p>
        <p><strong>Horário:</strong> {{timestamp}}</p>
        <hr>
        <p>Acesse o dashboard: <a href="https://dashboard.fazenda.com.br">https://dashboard.fazenda.com.br</a></p>
    </div>
</body>
</html>
```

### SMS

```
⚠️ {{tipo}}: {{mensagem}}. Setor: {{setor}}. Dashboard: https://bit.ly/fazenda
```

## 🧪 Testar Sistema

### Script de Teste

```bash
python send_test_alert.py
```

```python
# send_test_alert.py
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Invocar Lambda
lambda_client = boto3.client('lambda', region_name=os.getenv('AWS_REGION'))

payload = {
    "tipo": "Teste de Sistema",
    "mensagem": "Este é um teste do sistema de alertas",
    "severidade": "INFO",
    "setor": "Teste"
}

response = lambda_client.invoke(
    FunctionName='ProcessarAlertasFazenda',
    InvocationType='RequestResponse',
    Payload=json.dumps(payload)
)

print(response['Payload'].read().decode())
```

## 📊 Monitoramento

### CloudWatch Logs

```bash
# Ver logs recentes
aws logs tail /aws/lambda/ProcessarAlertasFazenda --follow

# Filtrar erros
aws logs filter-log-events \
  --log-group-name /aws/lambda/ProcessarAlertasFazenda \
  --filter-pattern "ERROR"
```

### Métricas

- Invocações por hora
- Erros
- Duração média
- Taxa de sucesso

## 🔒 Segurança

### IAM Role para Lambda

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish",
        "ses:SendEmail",
        "ses:SendRawEmail",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

## 💰 Custos

### Free Tier
- SNS: 1.000 notificações/mês grátis
- SES: 62.000 e-mails/mês grátis (via EC2)
- Lambda: 1M invocações/mês grátis

### Custos Estimados (após Free Tier)
- SNS SMS: $0.00645 por SMS (Brasil)
- SES: $0.10 por 1.000 e-mails
- Lambda: $0.20 por 1M invocações

## 📝 Checklist de Implementação

- [ ] Criar tópico SNS
- [ ] Subscrever números de telefone
- [ ] Verificar e-mails no SES
- [ ] Criar templates de mensagens
- [ ] Implementar função Lambda
- [ ] Configurar variáveis de ambiente
- [ ] Testar envio de SMS
- [ ] Testar envio de e-mail
- [ ] Integrar com dashboard
- [ ] Configurar triggers automáticos
- [ ] Capturar screenshots para documentação
- [ ] Monitorar logs no CloudWatch

## 🐛 Troubleshooting

### "Email address is not verified"
- Verificar e-mail no SES: `aws ses verify-email-identity --email-address seu@email.com`
- Aguardar e-mail de confirmação

### "SMS não enviado"
- Verificar se o país está suportado (Brasil: ✅)
- Verificar se há budget configurado
- Verificar IAM permissions

### "Lambda timeout"
- Aumentar timeout: `aws lambda update-function-configuration --timeout 60`

## 📦 Dependências

```
boto3
python-dotenv
jinja2 (para templates)
```
