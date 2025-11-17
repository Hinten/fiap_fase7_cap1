# Documentação do Projeto

Esta pasta contém toda a documentação técnica e prints de configuração do projeto.

## 📂 Conteúdo

### Documentação Técnica

- **arquitetura.md** - Diagrama e descrição da arquitetura do sistema
- **instalacao_detalhada.md** - Guia passo a passo de instalação
- **video_roteiro.md** - Roteiro para gravação do vídeo de apresentação

### Screenshots AWS

Pasta `aws_screenshots/` contém prints das configurações:

- SNS (SMS)
  - sns_topic_creation.png
  - sns_subscription.png
  - sns_test_message.png

- SES (E-mail)
  - ses_verified_identities.png
  - ses_template.png
  - ses_email_received.png

- Lambda
  - lambda_function.png
  - lambda_environment_variables.png
  - lambda_execution_logs.png

- CloudWatch
  - cloudwatch_logs.png
  - cloudwatch_metrics.png

- IAM
  - iam_role.png
  - iam_policies.png

## 📸 Captura de Screenshots

### Checklist AWS

- [ ] Criação de tópico SNS
- [ ] Subscrição de telefone no SNS
- [ ] Teste de envio SMS
- [ ] E-mails verificados no SES
- [ ] Template de e-mail no SES
- [ ] E-mail recebido (print da caixa de entrada)
- [ ] SMS recebido (foto do celular)
- [ ] Função Lambda criada
- [ ] Variáveis de ambiente da Lambda
- [ ] Logs de execução no CloudWatch
- [ ] Métricas no CloudWatch
- [ ] IAM Role e políticas

### Dicas para Screenshots

1. Use resolução adequada (1920x1080 ou maior)
2. Oculte informações sensíveis (IDs de conta, e-mails pessoais)
3. Capture a tela completa da AWS Console
4. Adicione anotações se necessário
5. Salve em formato PNG (melhor qualidade)

## 📝 Adicionar Nova Documentação

```bash
# Criar novo documento
cd docs
touch novo_documento.md

# Adicionar ao git
git add novo_documento.md
```
