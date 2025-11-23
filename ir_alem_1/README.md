# 🔍 Ir Além 1 - Integração AWS Rekognition

> **Projeto de Integração de IA na Infraestrutura AWS**  
> Implementação de reconhecimento de imagens usando AWS Rekognition para análise agrícola e aplicações diversas

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-Rekognition-orange.svg)](https://aws.amazon.com/rekognition/)
[![boto3](https://img.shields.io/badge/boto3-1.34+-green.svg)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Arquitetura](#-arquitetura)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração AWS](#-configuração-aws)
- [Como Usar](#-como-usar)
- [Campos Configuráveis](#-campos-configuráveis-do-rekognition)
- [Limitações do AWS Learner Lab](#-limitações-do-aws-learner-lab)
- [Casos de Uso](#-casos-de-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Justificativa Técnica](#-justificativa-técnica)
- [Screenshots](#-screenshots)
- [Vídeo Demonstrativo](#-vídeo-demonstrativo)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

Este projeto implementa uma solução completa de reconhecimento e análise de imagens utilizando **AWS Rekognition**, um serviço de visão computacional baseado em deep learning da Amazon Web Services. A solução foi desenvolvida como parte do desafio "Ir Além" da FIAP Fase 7 Cap 1, demonstrando a integração de IA na infraestrutura AWS.

### Objetivos

✅ Implementar análise de imagens usando AWS Rekognition  
✅ Criar uma API Python (boto3) flexível e reutilizável  
✅ Demonstrar casos de uso práticos (agrícola, segurança, OCR)  
✅ Documentar o processo de configuração na AWS  
✅ Fornecer exemplos de código comentados e explicativos  

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                    APLICAÇÃO PYTHON                          │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         RekognitionAnalyzer (boto3)                  │   │
│  │  - detect_labels()                                   │   │
│  │  - detect_faces()                                    │   │
│  │  - detect_text()                                     │   │
│  │  - detect_moderation_labels()                        │   │
│  │  - compare_faces()                                   │   │
│  └───────────────────┬──────────────────────────────────┘   │
│                      │                                       │
└──────────────────────┼───────────────────────────────────────┘
                       │
                       │ HTTPS/TLS
                       │ (boto3 SDK)
                       │
                       ▼
        ┌──────────────────────────────┐
        │      AWS CLOUD               │
        │                              │
        │  ┌────────────────────────┐  │
        │  │   AWS REKOGNITION      │  │
        │  │                        │  │
        │  │  • Computer Vision     │  │
        │  │  • Deep Learning       │  │
        │  │  • ML Models           │  │
        │  └────────────────────────┘  │
        │            │                 │
        │            │                 │
        │            ▼                 │
        │  ┌────────────────────────┐  │
        │  │   Amazon S3            │  │
        │  │   (Armazenamento)      │  │
        │  └────────────────────────┘  │
        │                              │
        └──────────────────────────────┘

┌─────────────────────────────────────────────┐
│  FONTES DE IMAGEM                           │
│                                             │
│  • Arquivo local (.jpg, .png)              │
│  • Bytes em memória                         │
│  • Amazon S3 Bucket                         │
└─────────────────────────────────────────────┘
```

### Fluxo de Processamento

1. **Upload/Envio da Imagem**: A aplicação carrega a imagem (local ou S3)
2. **Chamada API**: boto3 envia requisição HTTPS para AWS Rekognition
3. **Processamento**: Rekognition processa usando modelos de ML pré-treinados
4. **Resposta JSON**: Retorna resultados estruturados (labels, faces, texto, etc.)
5. **Formatação**: Aplicação processa e formata os resultados

---

## ✨ Funcionalidades

### 1. Detecção de Labels (Objetos e Cenas)
- Identifica objetos, cenas e conceitos em imagens
- Retorna nível de confiança para cada detecção
- Hierarquia de categorias (ex: Animal > Mamífero > Cachorro)
- **Aplicação**: Análise agrícola (tipo de cultura, condições do solo)

### 2. Detecção e Análise Facial
- Localiza rostos em imagens
- Analisa atributos: idade, emoções, acessórios
- Detecta características faciais (landmarks)
- **Aplicação**: Segurança, controle de acesso

### 3. Extração de Texto (OCR)
- Extrai texto de imagens
- Detecta texto em diversos idiomas
- Identifica palavras e linhas
- **Aplicação**: Digitalização de documentos, placas

### 4. Moderação de Conteúdo
- Detecta conteúdo impróprio ou sensível
- Categoriza por tipo de conteúdo
- **Aplicação**: Moderação em redes sociais, compliance

### 5. Comparação Facial
- Compara rostos entre duas imagens
- Retorna porcentagem de similaridade
- **Aplicação**: Verificação de identidade, autenticação

---

## 📦 Pré-requisitos

### Software Necessário

- **Python 3.8+** instalado
- **pip** (gerenciador de pacotes Python)
- **Conta AWS** (pode ser AWS Learner Lab)
- **Credenciais AWS** configuradas

### Conhecimentos Recomendados

- Python básico
- Conceitos de APIs REST
- Noções básicas de AWS
- Linha de comando (terminal)

---

## 🚀 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1/ir_alem_1
```

### 2. Crie um Ambiente Virtual (Recomendado)

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Credenciais AWS

Copie o arquivo de exemplo e edite com suas credenciais:

```bash
cp .env.example .env
nano .env  # ou use seu editor preferido
```

---

## 🔐 Configuração AWS

### Opção 1: AWS Learner Lab (Estudantes)

#### Passo a Passo com Screenshots

**1. Acesse o AWS Learner Lab**
   - Faça login no AWS Academy
   - Acesse o curso e clique em "Learner Lab"

**2. Inicie o Lab**
   - Clique no botão "Start Lab"
   - Aguarde até o indicador ficar verde

**3. Obtenha as Credenciais**
   - Clique em "AWS Details"
   - Clique em "Show" ao lado de "AWS CLI"
   - Copie as três linhas exibidas:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_SESSION_TOKEN`
   
**4. Configure no Projeto**
   - Cole as credenciais no arquivo `.env`
   - Ou exporte como variáveis de ambiente:

```bash
export AWS_ACCESS_KEY_ID='sua_access_key'
export AWS_SECRET_ACCESS_KEY='sua_secret_key'
export AWS_SESSION_TOKEN='seu_session_token'
export AWS_DEFAULT_REGION='us-east-1'
```

### Opção 2: Conta AWS Regular

#### Via AWS Console

1. Acesse **IAM** no console AWS
2. Crie um novo usuário ou use existente
3. Em "Security Credentials", crie uma **Access Key**
4. Copie o Access Key ID e Secret Access Key
5. Configure no arquivo `.env`

#### Via AWS CLI

```bash
aws configure
# Digite suas credenciais quando solicitado
```

---

## 💻 Como Usar

### Teste Rápido - Verificar Configuração

```bash
cd src
python aws_config.py
```

Este comando verifica se suas credenciais estão configuradas corretamente.

### Uso Básico - Análise de Imagem

```python
from src.rekognition_analyzer import RekognitionAnalyzer

# Inicializa o analisador
analyzer = RekognitionAnalyzer(region_name='us-east-1')

# Analisa uma imagem
response = analyzer.detect_labels(
    image_path='caminho/para/imagem.jpg',
    max_labels=10,
    min_confidence=80.0
)

# Formata e exibe os resultados
print(analyzer.format_labels_output(response))
```

### Exemplos Interativos

Execute o script de exemplos para testar as funcionalidades:

```bash
cd src
python example_usage.py
```

O script oferece um menu interativo com os seguintes casos de uso:

1. **Análise Agrícola** - Identifica culturas e condições de plantio
2. **Análise de Segurança** - Detecta pessoas e objetos
3. **Extração de Texto** - OCR para documentos e placas
4. **Moderação de Conteúdo** - Verifica conteúdo apropriado
5. **Comparação de Rostos** - Verifica identidade

### Exemplos de Código

#### Detectar Objetos e Cenas

```python
from src.rekognition_analyzer import RekognitionAnalyzer

analyzer = RekognitionAnalyzer()

# Detecta labels na imagem
response = analyzer.detect_labels(
    image_path='plantacao.jpg',
    max_labels=15,
    min_confidence=75.0
)

# Processa resultados
for label in response['Labels']:
    print(f"{label['Name']}: {label['Confidence']:.1f}%")
```

#### Detectar e Analisar Rostos

```python
# Detecta rostos com análise completa de atributos
response = analyzer.detect_faces(
    image_path='pessoa.jpg',
    attributes=['ALL']
)

# Analisa cada rosto detectado
for face in response['FaceDetails']:
    age_range = face['AgeRange']
    gender = face['Gender']['Value']
    emotions = face['Emotions']
    
    print(f"Idade: {age_range['Low']}-{age_range['High']}")
    print(f"Gênero: {gender}")
    print(f"Emoção principal: {emotions[0]['Type']}")
```

#### Extrair Texto (OCR)

```python
# Extrai texto da imagem
response = analyzer.detect_text(
    image_path='documento.jpg',
    min_confidence=80.0
)

# Imprime texto detectado
for text in response['TextDetections']:
    if text['Type'] == 'LINE':
        print(text['DetectedText'])
```

#### Comparar Rostos

```python
# Compara rostos entre duas imagens
response = analyzer.compare_faces(
    source_image_path='foto_referencia.jpg',
    target_image_path='foto_teste.jpg',
    similarity_threshold=80.0
)

# Verifica matches
if response['FaceMatches']:
    similarity = response['FaceMatches'][0]['Similarity']
    print(f"Similaridade: {similarity:.1f}%")
else:
    print("Nenhum rosto correspondente encontrado")
```

---

## ⚙️ Campos Configuráveis do Rekognition

### detect_labels()

| Campo | Tipo | Descrição | Valores |
|-------|------|-----------|---------|
| `MaxLabels` | Integer | Número máximo de labels a retornar | 1-1000 (padrão: 10) |
| `MinConfidence` | Float | Confiança mínima para incluir label | 0-100 (padrão: 80) |
| `Image` | Object | Fonte da imagem | Bytes ou S3Object |

**Exemplo de Configuração:**
```python
response = analyzer.detect_labels(
    image_path='imagem.jpg',
    max_labels=20,         # Retorna até 20 labels
    min_confidence=75.0    # Confiança mínima de 75%
)
```

**Justificativa dos Valores:**
- `MaxLabels=20`: Permite identificar mais elementos na análise agrícola
- `MinConfidence=75%`: Balance entre precisão e quantidade de resultados

### detect_faces()

| Campo | Tipo | Descrição | Valores |
|-------|------|-----------|---------|
| `Attributes` | List | Atributos faciais a analisar | ['DEFAULT'], ['ALL'] |
| `Image` | Object | Fonte da imagem | Bytes ou S3Object |

**Atributos Analisados com 'ALL':**
- **BoundingBox**: Localização do rosto na imagem (coordenadas)
- **AgeRange**: Faixa etária estimada (Low-High)
- **Gender**: Gênero estimado (Value, Confidence)
- **Emotions**: Emoções detectadas (Happy, Sad, Angry, etc.)
- **Smile**: Se está sorrindo (Value, Confidence)
- **Eyeglasses**: Se usa óculos
- **Sunglasses**: Se usa óculos escuros
- **Beard**: Se tem barba
- **Mustache**: Se tem bigode
- **EyesOpen**: Se os olhos estão abertos
- **MouthOpen**: Se a boca está aberta
- **Landmarks**: Pontos de referência faciais (olhos, nariz, boca)
- **Pose**: Orientação do rosto (Roll, Pitch, Yaw)
- **Quality**: Qualidade da imagem (Brightness, Sharpness)
- **Confidence**: Confiança na detecção do rosto

### detect_text()

| Campo | Tipo | Descrição | Valores |
|-------|------|-----------|---------|
| `Filters` | Object | Filtros para detecção | WordFilter, RegionsOfInterest |
| `MinConfidence` | Float | Confiança mínima (em Filters) | 0-100 |
| `Image` | Object | Fonte da imagem | Bytes ou S3Object |

**Tipos de Texto Detectado:**
- `LINE`: Linha completa de texto
- `WORD`: Palavra individual

### detect_moderation_labels()

| Campo | Tipo | Descrição | Valores |
|-------|------|-----------|---------|
| `MinConfidence` | Float | Confiança mínima | 0-100 (padrão: 60) |
| `Image` | Object | Fonte da imagem | Bytes ou S3Object |

**Categorias de Moderação:**
- Explicit Nudity
- Suggestive
- Violence
- Visually Disturbing
- Rude Gestures
- Drugs
- Tobacco
- Alcohol
- Gambling
- Hate Symbols

### compare_faces()

| Campo | Tipo | Descrição | Valores |
|-------|------|-----------|---------|
| `SourceImage` | Object | Imagem de referência | Bytes ou S3Object |
| `TargetImage` | Object | Imagem para comparar | Bytes ou S3Object |
| `SimilarityThreshold` | Float | Limiar de similaridade | 0-100 (padrão: 80) |
| `QualityFilter` | String | Filtro de qualidade | AUTO, NONE |

**Interpretação de Similaridade:**
- **95-100%**: Muito alta probabilidade de ser a mesma pessoa
- **85-94%**: Alta probabilidade
- **80-84%**: Provável
- **<80%**: Baixa probabilidade (não retornado por padrão)

---

## ⚠️ Limitações do AWS Learner Lab

### Restrições Conhecidas

1. **Créditos Limitados**
   - Orçamento mensal limitado (~$100 USD)
   - Monitore uso regularmente
   - Use com moderação para evitar bloqueio

2. **Tempo de Sessão**
   - Sessões expiram após 4 horas de inatividade
   - Credenciais precisam ser renovadas manualmente
   - `AWS_SESSION_TOKEN` é obrigatório

3. **Serviços Disponíveis**
   - Nem todos os serviços AWS estão disponíveis
   - Rekognition está disponível, mas com limitações
   - Verifique o catálogo de serviços do Learner Lab

4. **Regiões Disponíveis**
   - Geralmente limitado a `us-east-1` (N. Virginia)
   - Alguns recursos podem não estar em todas as regiões

5. **Permissões IAM**
   - Permissões pré-configuradas, não podem ser modificadas
   - Algumas operações administrativas podem estar bloqueadas

### Boas Práticas no Learner Lab

✅ **Faça testes com imagens pequenas** (< 1MB)  
✅ **Limite o número de chamadas à API** durante testes  
✅ **Documente com screenshots** antes de executar operações custosas  
✅ **Use o console AWS** para verificar custos acumulados  
✅ **Renove credenciais** sempre que iniciar uma nova sessão  

### Evidências de Configuração

Como o Learner Lab tem limitações de custo, é importante documentar o processo:

1. **Antes de Criar Recursos**: Tire screenshots das telas de configuração
2. **Console AWS**: Capture evidências do acesso ao Rekognition
3. **Documentação**: Explique cada campo configurado
4. **Código**: Mantenha código comentado mesmo sem execução total

---

## 🎯 Casos de Uso

### 1. Agricultura de Precisão

**Problema**: Identificar automaticamente o tipo de cultura e condições de plantio

**Solução**: 
```python
# Analisa imagem da plantação
response = analyzer.detect_labels(
    image_path='campo_soja.jpg',
    max_labels=20,
    min_confidence=70.0
)

# Identifica elementos agrícolas
agricultural_elements = [
    label for label in response['Labels']
    if any(term in label['Name'].lower() 
           for term in ['plant', 'crop', 'field', 'vegetation'])
]
```

**Benefícios**:
- Monitoramento automatizado de culturas
- Detecção precoce de problemas
- Otimização de recursos

### 2. Segurança Patrimonial

**Problema**: Monitorar áreas e detectar presenças não autorizadas

**Solução**:
```python
# Detecta pessoas e objetos
labels_response = analyzer.detect_labels(image_path='camera_seguranca.jpg')
faces_response = analyzer.detect_faces(image_path='camera_seguranca.jpg')

# Conta pessoas detectadas
person_count = sum(1 for label in labels_response['Labels'] 
                   if label['Name'] == 'Person')
face_count = len(faces_response['FaceDetails'])

# Gera alerta se necessário
if person_count > 0:
    send_security_alert(person_count, face_count)
```

**Benefícios**:
- Monitoramento 24/7 automatizado
- Alertas em tempo real
- Histórico de eventos

### 3. Digitalização de Documentos

**Problema**: Extrair informações de documentos físicos

**Solução**:
```python
# Extrai texto do documento
response = analyzer.detect_text(
    image_path='documento.jpg',
    min_confidence=85.0
)

# Organiza por linhas
lines = [t['DetectedText'] for t in response['TextDetections']
         if t['Type'] == 'LINE']

# Processa informações
documento_digitalizado = '\n'.join(lines)
```

**Benefícios**:
- Digitalização rápida
- Busca de conteúdo
- Arquivamento digital

---

## 📁 Estrutura do Projeto

```
ir_alem_1/
├── src/                              # Código fonte
│   ├── rekognition_analyzer.py       # Classe principal de análise
│   ├── example_usage.py              # Exemplos de uso
│   └── aws_config.py                 # Configuração de credenciais
│
├── examples/                         # Imagens de exemplo
│   ├── agricultural_field.jpg        # Exemplo agrícola
│   ├── security_camera.jpg           # Exemplo segurança
│   ├── document.jpg                  # Exemplo OCR
│   └── face1.jpg / face2.jpg        # Exemplo comparação
│
├── docs/                            # Documentação
│   ├── screenshots/                 # Prints do console AWS
│   │   ├── 01_start_lab.png
│   │   ├── 02_aws_details.png
│   │   ├── 03_rekognition_console.png
│   │   ├── 04_create_collection.png
│   │   └── 05_permissions.png
│   └── architecture.png             # Diagrama de arquitetura
│
├── requirements.txt                 # Dependências Python
├── .env.example                     # Exemplo de configuração
├── .gitignore                       # Arquivos ignorados
└── README.md                        # Este arquivo
```

---

## 💡 Justificativa Técnica

### Por que AWS Rekognition?

#### Vantagens

1. **Modelos Pré-treinados**
   - Não precisa treinar modelos do zero
   - Alta precisão desde o início
   - Economiza tempo e recursos computacionais

2. **Escalabilidade**
   - Processa de 1 a milhões de imagens
   - Infraestrutura gerenciada pela AWS
   - Sem necessidade de provisionar servidores

3. **Facilidade de Uso**
   - API simples e bem documentada
   - SDK boto3 em Python
   - Integração nativa com outros serviços AWS

4. **Custo-Benefício**
   - Pague apenas pelo uso (pay-as-you-go)
   - Sem custos iniciais de infraestrutura
   - Free tier disponível (conta regular)

#### Comparação com Alternativas

| Aspecto | AWS Rekognition | TensorFlow/PyTorch | Azure Computer Vision | Google Cloud Vision |
|---------|----------------|-------------------|----------------------|-------------------|
| Setup | ⭐⭐⭐⭐⭐ Simples | ⭐⭐ Complexo | ⭐⭐⭐⭐ Simples | ⭐⭐⭐⭐ Simples |
| Precisão | ⭐⭐⭐⭐ Alta | ⭐⭐⭐⭐⭐ Customizável | ⭐⭐⭐⭐ Alta | ⭐⭐⭐⭐ Alta |
| Escalabilidade | ⭐⭐⭐⭐⭐ Excelente | ⭐⭐ Manual | ⭐⭐⭐⭐⭐ Excelente | ⭐⭐⭐⭐⭐ Excelente |
| Custo Inicial | ⭐⭐⭐⭐⭐ Nenhum | ⭐⭐ Alto | ⭐⭐⭐⭐⭐ Nenhum | ⭐⭐⭐⭐⭐ Nenhum |
| Flexibilidade | ⭐⭐⭐ Média | ⭐⭐⭐⭐⭐ Total | ⭐⭐⭐ Média | ⭐⭐⭐ Média |

### Arquitetura Escolhida

#### Decisões de Design

1. **Classe Wrapper (`RekognitionAnalyzer`)**
   - Encapsula complexidade do boto3
   - Fornece interface intuitiva
   - Facilita manutenção e testes

2. **Separação de Responsabilidades**
   - `rekognition_analyzer.py`: Lógica de análise
   - `aws_config.py`: Gerenciamento de credenciais
   - `example_usage.py`: Demonstrações práticas

3. **Configuração Flexível**
   - Suporta múltiplas fontes de credenciais
   - Permite diferentes fontes de imagens
   - Parâmetros ajustáveis por chamada

4. **Tratamento de Erros**
   - Logging detalhado
   - Mensagens de erro claras
   - Validação de parâmetros

### Tecnologias Utilizadas

#### Python 3.8+
- **Motivo**: Linguagem moderna, grande comunidade, excelente para IA/ML
- **Vantagens**: Sintaxe clara, bibliotecas robustas, fácil manutenção

#### boto3 (AWS SDK)
- **Motivo**: SDK oficial da AWS para Python
- **Vantagens**: Bem documentado, mantido pela AWS, suporte completo

#### Pillow (PIL)
- **Motivo**: Manipulação de imagens
- **Vantagens**: Padrão da indústria, recursos completos

#### python-dotenv
- **Motivo**: Gerenciamento seguro de credenciais
- **Vantagens**: Separa configuração de código, previne commits acidentais

---

## 📸 Screenshots

### 1. Iniciando o AWS Learner Lab

![Iniciar Lab](docs/screenshots/01_start_lab.png)

*Passo 1: Clique em "Start Lab" e aguarde o indicador ficar verde*

### 2. Obtendo Credenciais AWS

![AWS Details](docs/screenshots/02_aws_details.png)

*Passo 2: Acesse "AWS Details" e copie as credenciais*

### 3. Console AWS Rekognition

![Rekognition Console](docs/screenshots/03_rekognition_console.png)

*Passo 3: Acesse o serviço Rekognition no console AWS*

### 4. Tela de Criação de Collection

![Create Collection](docs/screenshots/04_create_collection.png)

*Passo 4: Tela de configuração (antes de confirmar)*

### 5. Configuração de Permissões

![Permissions](docs/screenshots/05_permissions.png)

*Passo 5: Verificação das permissões IAM necessárias*

---

## 🎬 Vídeo Demonstrativo

### 📺 Link do Vídeo

> **🎥 [Assistir no YouTube](https://youtube.com/seu-video-aqui)** *(não listado)*

### Conteúdo do Vídeo (até 5 minutos)

1. **Introdução** (30s)
   - Apresentação do projeto
   - Objetivos e motivação

2. **Configuração AWS** (1min)
   - Demonstração do AWS Learner Lab
   - Obtenção de credenciais
   - Acesso ao Rekognition

3. **Código e Implementação** (2min)
   - Estrutura do projeto
   - Explicação das principais funções
   - Demonstração do código comentado

4. **Demonstração Prática** (1min 30s)
   - Execução de exemplos
   - Análise de resultados
   - Casos de uso práticos

5. **Conclusão** (30s)
   - Resumo dos resultados
   - Próximos passos
   - Referências

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📚 Referências

### Documentação Oficial

- [AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/)
- [boto3 Rekognition Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html)
- [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)

### Tutoriais e Guias

- [Getting Started with AWS Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html)
- [Best Practices for Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/best-practices.html)
- [AWS Learner Lab Guide](https://awsacademy.instructure.com/)

### Papers e Artigos

- [Deep Learning for Computer Vision](https://arxiv.org/abs/1803.08834)
- [Face Recognition: From Traditional to Deep Learning Methods](https://arxiv.org/abs/2001.00909)

---

## 👨‍💻 Autor

**FIAP - Fase 7 Cap 1**  
Projeto desenvolvido como parte do desafio "Ir Além"

---

## 🙏 Agradecimentos

- AWS pela infraestrutura e serviços
- FIAP pelo desafio proposto
- Comunidade Python e boto3
- AWS Academy e Learner Lab

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Made with ❤️ and ☕ for FIAP

</div>
