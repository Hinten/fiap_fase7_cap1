# Políticas IAM Necessárias para FarmTech Solutions

## Visão Geral

Este documento descreve as políticas IAM (Identity and Access Management) necessárias para o correto funcionamento do sistema de alertas AWS do projeto FarmTech Solutions.

## Princípio de Menor Privilégio

Seguimos o princípio de segurança de **menor privilégio**, concedendo apenas as permissões mínimas necessárias para o funcionamento do sistema.

---

## 1. Política SNS (Sistema de Alertas)

### Nome Sugerido: `FarmTech-SNS-Alerts-Policy`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SNSPublishAlerts",
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": "arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts"
    },
    {
      "Sid": "SNSGetTopicAttributes",
      "Effect": "Allow",
      "Action": [
        "sns:GetTopicAttributes"
      ],
      "Resource": "arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts"
    },
    {
      "Sid": "SNSListTopics",
      "Effect": "Allow",
      "Action": [
        "sns:ListTopics"
      ],
      "Resource": "*"
    }
  ]
}
```

**Permissões concedidas:**
- `sns:Publish` - Enviar mensagens para o tópico de alertas
- `sns:GetTopicAttributes` - Verificar status e configuração do tópico (usado no test_connection)
- `sns:ListTopics` - Listar tópicos disponíveis (opcional, para diagnóstico)

**Recursos:**
- Específico ao tópico `farm-alerts`
- Substitua `ACCOUNT_ID` pelo ID da sua conta AWS (12 dígitos)

---

## 2. Política SES (Email - Opcional)

Se optar por usar SES em vez de SNS para emails:

### Nome Sugerido: `FarmTech-SES-Email-Policy`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SESendEmail",
      "Effect": "Allow",
      "Action": [
        "ses:SendEmail",
        "ses:SendRawEmail"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ses:FromAddress": "noreply@farmtech.com"
        }
      }
    },
    {
      "Sid": "SESGetIdentity",
      "Effect": "Allow",
      "Action": [
        "ses:GetIdentityVerificationAttributes",
        "ses:ListIdentities"
      ],
      "Resource": "*"
    }
  ]
}
```

**Nota:** Requer verificação de domínio/email no SES.

---

## 3. Criação do Usuário IAM

### Via Console AWS

1. Acessar **IAM Console** → Users → Create user
2. Nome do usuário: `farmtech-app`
3. Tipo de acesso: **Programmatic access** (Access key)
4. Anexar política: `FarmTech-SNS-Alerts-Policy` (criada acima)
5. Criar usuário e **salvar as credenciais**:
   - Access Key ID (ex: `AKIAIOSFODNN7EXAMPLE`)
   - Secret Access Key (ex: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`)

### Via AWS CLI

```bash
# Criar usuário
aws iam create-user --user-name farmtech-app

# Criar política (salve o JSON em farmtech-sns-policy.json)
aws iam create-policy \
  --policy-name FarmTech-SNS-Alerts-Policy \
  --policy-document file://farmtech-sns-policy.json

# Anexar política ao usuário
aws iam attach-user-policy \
  --user-name farmtech-app \
  --policy-arn arn:aws:iam::ACCOUNT_ID:policy/FarmTech-SNS-Alerts-Policy

# Criar access key
aws iam create-access-key --user-name farmtech-app
```

---

## 4. Configuração do Tópico SNS

### Criar Tópico

```bash
# Criar tópico SNS
aws sns create-topic --name farm-alerts --region us-east-1

# Saída:
# {
#   "TopicArn": "arn:aws:sns:us-east-1:123456789012:farm-alerts"
# }
```

### Adicionar Assinaturas

#### Email

```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts \
  --protocol email \
  --notification-endpoint contato@farmtech.com
```

**⚠️ Importante:** Confirme a assinatura acessando o link enviado para o email.

#### SMS

```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts \
  --protocol sms \
  --notification-endpoint +5511999999999
```

**Nota:** SMS requer configuração adicional:
- Verificação de número (sandbox mode)
- Configuração de SMS preferences (custos aplicam)

### Política de Acesso do Tópico

Para permitir publicação:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowFarmTechPublish",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_ID:user/farmtech-app"
      },
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:us-east-1:ACCOUNT_ID:farm-alerts"
    }
  ]
}
```

---

## 5. Variáveis de Ambiente (.env)

Após criar o usuário e tópico, configure no `.env`:

```env
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=us-east-1
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789012:farm-alerts
```

---

## 6. Teste de Permissões

Execute o teste de conexão para validar as configurações:

```python
from src.fase5.aws.alert_service import test_aws_connection

result = test_aws_connection()
print(result)
```

**Resultado esperado:**
```python
{
  "status": "success",
  "topic_arn": "arn:aws:sns:us-east-1:...:farm-alerts",
  "topic_name": "FarmTech Alerts",
  "subscriptions_confirmed": "2",
  "subscriptions_pending": "0"
}
```

---

## 7. Custos AWS

### SNS (Free Tier)

- **Primeiro 1.000 publicações/mês**: Gratuito
- **Primeiros 1.000 emails/mês**: Gratuito
- **Primeiros 100 SMS/mês**: Gratuito (pode variar por região)

### Após Free Tier

- **Publicações adicionais**: ~$0.50 por 1 milhão
- **Emails adicionais**: ~$2.00 por 100.000
- **SMS Brasil**: ~$0.05 por SMS

**Estimativa mensal (uso moderado):**
- 500 alertas/mês → **Gratuito** (dentro do free tier)
- 2.000 alertas/mês → ~$0.50

---

## 8. Segurança e Boas Práticas

### ✅ Recomendações

1. **Rotação de Chaves**: Rotacione access keys a cada 90 dias
2. **MFA**: Ative MFA na conta root AWS
3. **Secrets Manager**: Em produção, use AWS Secrets Manager ou Parameter Store
4. **CloudTrail**: Ative para auditoria de ações
5. **Alertas de Custos**: Configure billing alerts
6. **Restrição de IP**: Adicione condição de IP na política (se IP fixo)

### ❌ Evitar

1. Nunca commite credenciais no Git
2. Não use credenciais da conta root
3. Não conceda permissões `*` (all actions)
4. Não compartilhe access keys

### Exemplo com Restrição de IP

```json
{
  "Condition": {
    "IpAddress": {
      "aws:SourceIp": ["203.0.113.0/24"]
    }
  }
}
```

---

## 9. Troubleshooting

### Erro: "AccessDenied"

**Causa:** Política IAM insuficiente

**Solução:**
1. Verificar se política está anexada ao usuário
2. Validar ARN do tópico no Resource da política
3. Aguardar alguns minutos (propagação de permissões)

### Erro: "InvalidClientTokenId"

**Causa:** Access Key inválida ou desabilitada

**Solução:**
1. Verificar credenciais no `.env`
2. Recriar access key no IAM
3. Verificar se usuário existe

### Erro: "NotFound"

**Causa:** Tópico SNS não existe ou ARN incorreto

**Solução:**
```bash
# Listar tópicos existentes
aws sns list-topics --region us-east-1
```

---

## 10. Checklist de Configuração

- [ ] Usuário IAM `farmtech-app` criado
- [ ] Política `FarmTech-SNS-Alerts-Policy` criada e anexada
- [ ] Tópico SNS `farm-alerts` criado
- [ ] Assinatura de email adicionada e confirmada
- [ ] Access Key criada e salva
- [ ] Variáveis `.env` configuradas
- [ ] Teste de conexão executado com sucesso
- [ ] Alerta de teste enviado e recebido
- [ ] Billing alert configurado

---

## Referências

- [AWS SNS Documentation](https://docs.aws.amazon.com/sns/)
- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [boto3 SNS Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html)

---

**Última Atualização:** 17/11/2025  
**Responsável:** Grupo 28 - FIAP
