# Fase 5: Cloud Computing & Segurança

## 📋 Descrição

Infraestrutura na AWS com padrões de segurança ISO 27001 e ISO 27002.

## 🎯 Objetivos

- Hospedagem em AWS (EC2, RDS, S3)
- Configuração de segurança (IAM, Security Groups)
- Aplicação de normas ISO 27001/27002
- Backup automático
- Monitoramento com CloudWatch
- Escalabilidade

## 📂 Estrutura

```
phase5/
├── infraestrutura/    # Templates CloudFormation/Terraform
├── scripts_deploy/    # Scripts de deploy AWS
└── seguranca/         # Documentação ISO 27001/27002
```

## ☁️ Serviços AWS Utilizados

### Compute
- **EC2**: Hospedagem da aplicação
  - Tipo: t2.micro (Free Tier) ou t3.medium
  - OS: Ubuntu 22.04 LTS
  - Security Group: HTTP (80), HTTPS (443), SSH (22)

### Database
- **RDS PostgreSQL**: Banco de dados gerenciado
  - Versão: PostgreSQL 15
  - Storage: 20GB GP2
  - Backups automáticos diários

### Storage
- **S3**: Armazenamento de objetos
  - Buckets:
    - `fazenda-imagens`: Imagens para YOLO
    - `fazenda-backups`: Backups do sistema
    - `fazenda-logs`: Logs de aplicação

### Networking
- **VPC**: Rede privada virtual
- **Subnets**: Públicas e privadas
- **Internet Gateway**: Acesso à internet
- **NAT Gateway**: Para subnets privadas

### Monitoring & Logs
- **CloudWatch**: Métricas e logs
  - CPU utilization
  - Network I/O
  - Disk usage
  - Application logs

### Security
- **IAM**: Controle de acesso
  - Roles para EC2, Lambda
  - Policies com princípio do menor privilégio
- **Security Groups**: Firewall de instâncias
- **KMS**: Criptografia de dados

## 🔧 Como Usar

### Deploy com CloudFormation

```bash
cd phase5/infraestrutura
aws cloudformation create-stack \
  --stack-name fazenda-stack \
  --template-body file://template.yaml \
  --capabilities CAPABILITY_IAM
```

### Deploy com Terraform

```bash
cd phase5/infraestrutura
terraform init
terraform plan
terraform apply
```

### Deploy Manual via Scripts

```bash
cd phase5/scripts_deploy
bash deploy_ec2.sh
bash setup_rds.sh
bash configure_s3.sh
```

## 🔒 Segurança

### Checklist ISO 27001/27002

- [ ] Política de segurança da informação
- [ ] Controle de acesso baseado em roles (RBAC)
- [ ] Criptografia em trânsito (TLS/SSL)
- [ ] Criptografia em repouso (AWS KMS)
- [ ] Autenticação multifator (MFA)
- [ ] Backups automáticos e testados
- [ ] Logs de auditoria centralizados
- [ ] Plano de resposta a incidentes
- [ ] Revisão periódica de permissões

### Boas Práticas Implementadas

1. **Principle of Least Privilege**: Permissões mínimas necessárias
2. **Defense in Depth**: Múltiplas camadas de segurança
3. **Separation of Concerns**: Ambientes dev/prod separados
4. **Data Encryption**: Dados sensíveis sempre criptografados
5. **Regular Updates**: Sistema operacional e bibliotecas atualizadas

## 📦 Dependências Específicas

```
boto3
awscli
```

## 🔗 Repositório Original

[fiap_fase5_cap1](https://github.com/Hinten/fiap_fase5_cap1)

## 📝 O Que Trazer do Repositório Original

- Templates de infraestrutura (CloudFormation/Terraform)
- Scripts de deploy
- Configurações IAM
- Documentação de segurança
- Políticas e procedures ISO
- Scripts de backup
- Configurações de monitoramento
