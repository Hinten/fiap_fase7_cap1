# 🎬 Roteiro para Vídeo Demonstrativo

**Duração Total**: Máximo 5 minutos  
**Objetivo**: Demonstrar a integração AWS Rekognition implementada

---

## 🎯 Estrutura do Vídeo

### 0:00 - 0:30 | INTRODUÇÃO (30 segundos)

**Visual**: Tela inicial com título do projeto

**Narração**:
> "Olá! Neste vídeo, vou apresentar a implementação do desafio 'Ir Além' da FIAP Fase 7 Cap 1, onde desenvolvi uma solução de reconhecimento de imagens usando AWS Rekognition."

**Pontos a mencionar**:
- Nome do projeto: "Integração AWS Rekognition"
- Objetivo: Análise inteligente de imagens usando IA na AWS
- Tecnologias: Python, boto3, AWS Rekognition

**Tela**:
- README do projeto aberto
- Logo da AWS e Python visíveis

---

### 0:30 - 1:30 | CONFIGURAÇÃO AWS (1 minuto)

**Visual**: AWS Learner Lab e Console

**Narração**:
> "Primeiro, vou mostrar como configurei o ambiente AWS. Usando o AWS Learner Lab, iniciei a sessão e obtive as credenciais necessárias."

**Demonstração**:

1. **Iniciar Lab** (0:30 - 0:45)
   - Mostrar tela do Learner Lab
   - Clicar em "Start Lab"
   - Aguardar indicador verde
   - **Screenshot**: `01_start_lab.png`

2. **Obter Credenciais** (0:45 - 1:00)
   - Clicar em "AWS Details"
   - Clicar em "Show" ao lado de "AWS CLI"
   - Mostrar as três linhas de credenciais (mascaradas)
   - **Screenshot**: `02_aws_details.png`

3. **Console Rekognition** (1:00 - 1:30)
   - Acessar AWS Console
   - Buscar "Rekognition"
   - Mostrar página inicial do serviço
   - **Screenshot**: `03_rekognition_console.png`
   - Explicar campos importantes:
     - Region (us-east-1)
     - Serviços disponíveis
     - Limitações do Learner Lab

**Pontos a mencionar**:
- Session token obrigatório no Learner Lab
- Credenciais expiram após 4 horas
- Serviço está disponível, mas com limites de custo
- Prints comprovam acesso ao serviço

---

### 1:30 - 3:00 | CÓDIGO E IMPLEMENTAÇÃO (1 minuto 30 segundos)

**Visual**: VS Code ou editor com código aberto

**Narração**:
> "Agora vou mostrar a implementação em Python. Desenvolvi uma classe wrapper para o boto3 que simplifica o uso do Rekognition."

**Demonstração**:

1. **Estrutura do Projeto** (1:30 - 1:45)
   ```
   ir_alem_1/
   ├── src/
   │   ├── rekognition_analyzer.py  ← Classe principal
   │   ├── example_usage.py         ← Exemplos
   │   └── aws_config.py            ← Credenciais
   ├── examples/                    ← Imagens teste
   ├── docs/screenshots/            ← Prints AWS
   └── README.md                    ← Documentação
   ```

2. **Classe RekognitionAnalyzer** (1:45 - 2:15)
   - Abrir `rekognition_analyzer.py`
   - Mostrar métodos principais:
     ```python
     def detect_labels(...)      # Detecta objetos
     def detect_faces(...)       # Detecta rostos
     def detect_text(...)        # OCR
     def detect_moderation_labels(...)  # Moderação
     def compare_faces(...)      # Comparação facial
     ```
   - Destacar comentários em português
   - Mostrar docstrings explicativas

3. **Configuração de Credenciais** (2:15 - 2:30)
   - Mostrar arquivo `.env.example`
   - Explicar como configurar:
     ```
     AWS_ACCESS_KEY_ID=...
     AWS_SECRET_ACCESS_KEY=...
     AWS_SESSION_TOKEN=...
     AWS_DEFAULT_REGION=us-east-1
     ```

4. **Campos Configuráveis** (2:30 - 3:00)
   - Explicar parâmetros principais:
     - `max_labels`: Quantos objetos detectar (padrão: 10)
     - `min_confidence`: Confiança mínima (padrão: 80%)
     - `attributes`: Quais atributos faciais analisar (DEFAULT/ALL)
   - Justificar escolhas dos valores padrão

**Pontos a mencionar**:
- Código totalmente comentado
- Suporte a múltiplas fontes de imagem (local, bytes, S3)
- Tratamento de erros robusto
- Interface intuitiva

---

### 3:00 - 4:30 | DEMONSTRAÇÃO PRÁTICA (1 minuto 30 segundos)

**Visual**: Terminal executando o código

**Narração**:
> "Vamos ver o sistema funcionando na prática. Vou demonstrar três casos de uso diferentes."

**Demonstração**:

1. **Verificação de Setup** (3:00 - 3:15)
   ```bash
   cd src
   python setup_check.py
   ```
   - Mostrar todas as verificações passando (✓)
   - Credenciais configuradas
   - Dependências instaladas

2. **Análise de Imagem Agrícola** (3:15 - 3:40)
   ```bash
   python example_usage.py
   # Escolher opção 1: Análise Agrícola
   ```
   - Mostrar imagem de entrada (campo/plantação)
   - Executar análise
   - Mostrar resultados:
     ```
     Labels detectados:
     • Plant: 98.5% de confiança
     • Field: 96.2% de confiança
     • Agriculture: 94.8% de confiança
     • Vegetation: 92.3% de confiança
     ```

3. **Detecção de Rostos** (3:40 - 4:00)
   ```bash
   # Escolher opção 2 ou usar detect_faces
   ```
   - Mostrar imagem com rosto
   - Executar análise facial
   - Mostrar atributos detectados:
     ```
     Rosto 1:
     • Idade estimada: 25-35 anos
     • Emoção: Happy (95.2%)
     • Óculos: Não (98.1%)
     • Sorrindo: Sim (94.5%)
     ```

4. **OCR - Extração de Texto** (4:00 - 4:30)
   ```bash
   # Escolher opção 3: Extração de Texto
   ```
   - Mostrar imagem com texto (placa, documento)
   - Executar OCR
   - Mostrar texto extraído:
     ```
     Textos detectados:
     • "STOP" - 99.1% confiança
     • "Speed Limit 50" - 97.8% confiança
     ```

**Pontos a mencionar**:
- Resultados em tempo real
- Alta precisão (> 90%)
- Múltiplos casos de uso
- Fácil de usar

---

### 4:30 - 5:00 | CONCLUSÃO (30 segundos)

**Visual**: Arquitetura do projeto / README

**Narração**:
> "Como vimos, a solução implementa com sucesso a integração do AWS Rekognition, oferecendo análise inteligente de imagens com alta precisão. O código está totalmente documentado e pronto para uso."

**Resumir**:
1. **Configuração AWS**:
   - Learner Lab configurado
   - Credenciais obtidas
   - Acesso ao Rekognition comprovado

2. **Implementação**:
   - 5 funcionalidades principais
   - Código comentado em português
   - Exemplos práticos

3. **Resultados**:
   - Sistema funcionando
   - Alta precisão nas análises
   - Fácil de estender

4. **Próximos Passos**:
   - Adicionar mais casos de uso
   - Integrar com aplicações
   - Escalar para produção

**Tela Final**:
- GitHub: `https://github.com/Hinten/fiap_fase7_cap1/tree/main/ir_alem_1`
- "Obrigado por assistir!"
- Contato/Email

---

## 🎥 Dicas de Gravação

### Preparação

1. **Ambiente**:
   - Limpe o desktop
   - Feche janelas desnecessárias
   - Use tema escuro no editor (melhor visibilidade)
   - Aumente tamanho da fonte (mínimo 16pt)

2. **Audio**:
   - Use microfone decente
   - Ambiente silencioso
   - Teste antes de gravar
   - Fale claramente e pausadamente

3. **Visual**:
   - Resolução 1920x1080 ou superior
   - Gravador de tela (OBS Studio, Zoom, QuickTime)
   - Mostre cursor do mouse
   - Use zoom quando necessário

### Durante a Gravação

1. **Ritmo**:
   - Não corra
   - Pause entre seções
   - Dê tempo para leituras
   - Máximo 5 minutos!

2. **Demonstrações**:
   - Prepare arquivos com antecedência
   - Teste tudo antes
   - Tenha backup se algo falhar
   - Screenshots prontos para mostrar

3. **Narração**:
   - Seja natural
   - Explique o que está fazendo
   - Destaque pontos importantes
   - Seja entusiasmado mas profissional

### Edição

1. **Cortes**:
   - Remova pausas longas
   - Corte erros
   - Mantenha transições suaves

2. **Adições**:
   - Texto sobreposto para pontos-chave
   - Zoom em áreas importantes
   - Setas/círculos para destacar
   - Música de fundo suave (opcional, baixo volume)

3. **Qualidade**:
   - Exportar em HD (1080p)
   - Formato MP4 (H.264)
   - Taxa de bits adequada
   - Audio sincronizado

### Publicação

1. **YouTube**:
   - Título: "AWS Rekognition - Integração IA FIAP Fase 7"
   - Descrição: Link do GitHub + resumo
   - Tags: AWS, Rekognition, Python, IA, FIAP
   - Visibilidade: "Não listado"

2. **Miniatura**:
   - Use logo AWS + Python
   - Texto: "AWS Rekognition"
   - Cores vibrantes
   - 1280x720 pixels

3. **Descrição do Vídeo**:
   ```
   Demonstração da integração AWS Rekognition desenvolvida para o 
   desafio "Ir Além" da FIAP Fase 7 Cap 1.
   
   🔗 GitHub: https://github.com/Hinten/fiap_fase7_cap1/tree/main/ir_alem_1
   
   📋 Funcionalidades:
   • Detecção de objetos e cenas
   • Análise facial e atributos
   • Extração de texto (OCR)
   • Moderação de conteúdo
   • Comparação facial
   
   🛠️ Tecnologias:
   • Python 3.8+
   • AWS Rekognition
   • boto3
   
   ⏱️ Timestamps:
   0:00 - Introdução
   0:30 - Configuração AWS
   1:30 - Código e Implementação
   3:00 - Demonstração Prática
   4:30 - Conclusão
   ```

---

## ✅ Checklist Final

Antes de gravar:
- [ ] Ambiente limpo e organizado
- [ ] Código funcionando 100%
- [ ] Imagens de teste preparadas
- [ ] Screenshots AWS salvos
- [ ] Microfone testado
- [ ] Gravador de tela configurado
- [ ] Roteiro revisado
- [ ] Tempo cronometrado (<5min)

Após gravar:
- [ ] Vídeo editado
- [ ] Audio claro
- [ ] Duração <= 5 minutos
- [ ] Qualidade HD
- [ ] Miniatura criada
- [ ] Descrição completa
- [ ] Upload no YouTube (não listado)
- [ ] Link adicionado ao README

---

**Boa sorte com a gravação! 🎬🚀**
