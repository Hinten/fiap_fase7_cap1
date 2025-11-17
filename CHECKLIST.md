# ✅ Checklist de Implementação - Fase 7

Use este checklist para acompanhar o progresso da implementação completa do projeto.

---

## 📋 Fase 1: Preparação e Inventário

### Clonar Repositórios Originais
- [ ] Clonar fiap_fase1_cap1
- [ ] Clonar fiap_fase2_cap1
- [ ] Clonar fiap_fase3_cap1-novo
- [ ] Clonar fiap_fase4_cap1
- [ ] Clonar fiap_fase5_cap1
- [ ] Clonar fiap_fase6_cap1

### Inventariar Código
- [ ] Listar arquivos principais da Fase 1
- [ ] Listar arquivos principais da Fase 2
- [ ] Listar arquivos principais da Fase 3
- [ ] Listar arquivos principais da Fase 4
- [ ] Listar arquivos principais da Fase 5
- [ ] Listar arquivos principais da Fase 6

---

## 📋 Fase 2: Migração de Código

### Fase 1: Meteorologia
- [ ] Migrar scripts de cálculo de área
- [ ] Migrar integração API meteorológica
- [ ] Migrar scripts R de análise
- [ ] Testar execução isolada
- [ ] Atualizar requirements.txt

### Fase 2: Banco de Dados
- [ ] Copiar diagramas MER/DER
- [ ] Migrar scripts SQL
- [ ] Migrar modelos ORM
- [ ] Criar migrations com Alembic
- [ ] Testar conexão com BD

### Fase 3: IoT
- [ ] Copiar firmware ESP32
- [ ] Migrar simulador de sensores
- [ ] Migrar API CRUD
- [ ] Testar simulador
- [ ] Testar API

### Fase 4: Machine Learning
- [ ] Copiar aplicação Streamlit original
- [ ] Migrar modelos ML (.pkl)
- [ ] Migrar notebooks
- [ ] Testar modelos
- [ ] Validar previsões

### Fase 5: AWS
- [ ] Copiar templates de infraestrutura
- [ ] Copiar scripts de deploy
- [ ] Revisar documentação de segurança
- [ ] Atualizar para contexto atual

### Fase 6: Visão Computacional
- [ ] Copiar modelo YOLO (.pt)
- [ ] Migrar scripts de inferência
- [ ] Copiar imagens de exemplo
- [ ] Testar detecção
- [ ] Validar resultados

---

## 📋 Fase 3: Integração

### Banco de Dados
- [ ] Executar setup_database.py
- [ ] Executar seed_data.py
- [ ] Verificar tabelas criadas
- [ ] Testar queries básicas

### Dashboard Unificada
- [ ] Implementar página Fase 1
- [ ] Implementar página Fase 2
- [ ] Implementar página Fase 3
- [ ] Implementar página Fase 4
- [ ] Implementar página Fase 6
- [ ] Implementar página Alertas
- [ ] Testar navegação
- [ ] Testar botões de ação

### Integração de Serviços
- [ ] Conectar Fase 1 → Banco de Dados
- [ ] Conectar Fase 3 → Banco de Dados
- [ ] Conectar Fase 4 → Modelos ML
- [ ] Conectar Fase 6 → YOLO
- [ ] Testar fluxo completo

---

## 📋 Fase 4: Sistema de Alertas AWS

### Configurar SNS (SMS)
- [ ] Criar conta AWS (se não tiver)
- [ ] Criar tópico SNS
- [ ] Subscrever número de telefone
- [ ] Configurar SMS preferences
- [ ] Testar envio de SMS
- [ ] Capturar screenshot: criação do tópico
- [ ] Capturar screenshot: subscrição
- [ ] Capturar screenshot: SMS recebido (foto do celular)

### Configurar SES (E-mail)
- [ ] Verificar e-mail remetente
- [ ] Verificar e-mails destinatários
- [ ] Criar template de e-mail
- [ ] Solicitar saída do sandbox (opcional)
- [ ] Testar envio de e-mail
- [ ] Capturar screenshot: identidades verificadas
- [ ] Capturar screenshot: template
- [ ] Capturar screenshot: e-mail recebido

### Criar Função Lambda
- [ ] Escrever código lambda_handler.py
- [ ] Empacotar função (zip)
- [ ] Criar IAM role
- [ ] Deploy da função
- [ ] Configurar variáveis de ambiente
- [ ] Testar função
- [ ] Capturar screenshot: função criada
- [ ] Capturar screenshot: variáveis de ambiente
- [ ] Capturar screenshot: logs CloudWatch

### Integrar com Dashboard
- [ ] Implementar chamada à Lambda
- [ ] Testar envio de alerta pela dashboard
- [ ] Validar recebimento de e-mail e SMS
- [ ] Criar histórico de alertas no BD

---

## 📋 Fase 5: Testes

### Testes Individuais
- [ ] Testar Fase 1 isoladamente
- [ ] Testar Fase 2 isoladamente
- [ ] Testar Fase 3 isoladamente
- [ ] Testar Fase 4 isoladamente
- [ ] Testar Fase 6 isoladamente
- [ ] Testar sistema de alertas

### Testes de Integração
- [ ] Testar fluxo: Sensor → BD → Alerta
- [ ] Testar fluxo: Meteorologia → BD → Dashboard
- [ ] Testar fluxo: YOLO → Detecção → Alerta
- [ ] Testar fluxo: ML → Previsão → Recomendação

### Testes de Performance
- [ ] Testar tempo de resposta da dashboard
- [ ] Testar latência das APIs
- [ ] Testar carga no banco de dados
- [ ] Validar limites de alertas

---

## 📋 Fase 6: Documentação

### Atualizar Documentação
- [ ] Revisar README.md
- [ ] Atualizar instruções de instalação
- [ ] Adicionar troubleshooting específico
- [ ] Documentar decisões de design

### Screenshots AWS
- [ ] Organizar screenshots na pasta docs/aws_screenshots/
- [ ] Adicionar legendas/anotações se necessário
- [ ] Criar documento docs/aws_configuration.md
- [ ] Listar custos AWS utilizados

### Preparar para Vídeo
- [ ] Criar roteiro detalhado
- [ ] Preparar dados de demonstração
- [ ] Testar todos os fluxos
- [ ] Preparar ambiente limpo

---

## 📋 Fase 7: Vídeo de Apresentação

### Preparação
- [ ] Limpar ambiente de desenvolvimento
- [ ] Preparar dados frescos no BD
- [ ] Ter imagens prontas para YOLO
- [ ] Testar dashboard completamente
- [ ] Abrir prints AWS em abas do navegador

### Gravação
- [ ] Configurar software de gravação
- [ ] Testar áudio
- [ ] Ensaiar uma vez
- [ ] Gravar vídeo (máx 10 min)
- [ ] Revisar gravação

### Edição
- [ ] Cortar pausas longas
- [ ] Adicionar transições
- [ ] Verificar áudio
- [ ] Adicionar introdução/conclusão

### Upload
- [ ] Criar conta YouTube (se necessário)
- [ ] Fazer upload
- [ ] Configurar como "Não listado"
- [ ] Adicionar título e descrição
- [ ] Copiar link
- [ ] Adicionar link ao README.md

---

## 📋 Fase 8: Revisão Final e Entrega

### Checklist de Qualidade
- [ ] Todos os scripts executam sem erros
- [ ] Dashboard carrega corretamente
- [ ] Todos os botões funcionam
- [ ] Não há erros no console
- [ ] Código está comentado
- [ ] READMEs estão completos
- [ ] Link do vídeo está no README
- [ ] Screenshots AWS estão na pasta docs/

### Teste Final Completo
- [ ] Clonar repositório em ambiente limpo
- [ ] Seguir instruções do README do zero
- [ ] Executar setup_database.py
- [ ] Executar seed_data.py
- [ ] Iniciar dashboard
- [ ] Testar todas as páginas
- [ ] Enviar alerta teste
- [ ] Verificar recebimento

### Preparar Entrega
- [ ] Fazer commit final
- [ ] Push para GitHub
- [ ] Verificar que repositório está público (ou adicionar @leoruiz197)
- [ ] Verificar que .env não foi commitado
- [ ] Criar PDF com link do GitHub
- [ ] Incluir nomes dos integrantes
- [ ] Incluir link do vídeo no PDF

### Submissão
- [ ] Fazer upload do PDF no portal FIAP
- [ ] Verificar prazo de entrega
- [ ] Confirmar submissão
- [ ] NÃO fazer commits após o prazo

---

## 📊 Estatísticas de Progresso

**Total de Itens**: 113 tarefas

**Por Fase**:
- Fase 1 (Preparação): 12 itens
- Fase 2 (Migração): 30 itens
- Fase 3 (Integração): 19 itens
- Fase 4 (AWS): 26 itens
- Fase 5 (Testes): 13 itens
- Fase 6 (Documentação): 8 itens
- Fase 7 (Vídeo): 13 itens
- Fase 8 (Entrega): 15 itens

---

## 📝 Notas

- Marque cada item quando concluído
- Documente problemas encontrados
- Mantenha commits frequentes
- Peça ajuda quando necessário
- Não deixe para a última hora

---

## 🎯 Meta Final

✅ Sistema completo integrado  
✅ Documentação abrangente  
✅ Vídeo demonstrativo  
✅ Entrega no prazo  

**Boa sorte!** 🚀
