# 🔧 Guia de Solução de Problemas

Este documento lista problemas comuns e suas soluções ao usar o projeto AWS Rekognition.

---

## 📋 Índice

1. [Problemas de Instalação](#problemas-de-instalação)
2. [Problemas de Credenciais AWS](#problemas-de-credenciais-aws)
3. [Problemas com o Rekognition](#problemas-com-o-rekognition)
4. [Problemas do AWS Learner Lab](#problemas-do-aws-learner-lab)
5. [Problemas de Execução](#problemas-de-execução)
6. [Erros Comuns da API](#erros-comuns-da-api)

---

## 🐍 Problemas de Instalação

### Erro: `ModuleNotFoundError: No module named 'boto3'`

**Causa**: boto3 não está instalado

**Solução**:
```bash
pip install boto3
# ou instale todas as dependências
pip install -r requirements.txt
```

---

### Erro: `pip: command not found`

**Causa**: pip não está instalado ou não está no PATH

**Solução**:

**Opção 1 - Instalar pip:**
```bash
# Linux/Mac
sudo apt-get install python3-pip  # Ubuntu/Debian
brew install python3              # Mac

# Windows
# Baixe get-pip.py e execute
python get-pip.py
```

**Opção 2 - Usar python -m pip:**
```bash
python -m pip install -r requirements.txt
```

---

### Erro: `Python version 3.6 not supported`

**Causa**: Python muito antigo (precisa 3.8+)

**Solução**:
```bash
# Verifique a versão
python --version

# Se < 3.8, instale versão mais nova:
# Linux
sudo apt-get install python3.10

# Mac
brew install python@3.10

# Windows
# Baixe do site oficial: https://www.python.org/downloads/
```

---

### Erro: `permission denied` durante instalação

**Causa**: Falta de permissões

**Solução**:

**Opção 1 - Ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**Opção 2 - Instalar para usuário:**
```bash
pip install --user -r requirements.txt
```

**Opção 3 - Usar sudo (não recomendado):**
```bash
sudo pip install -r requirements.txt
```

---

## 🔐 Problemas de Credenciais AWS

### Erro: `Unable to locate credentials`

**Causa**: Credenciais AWS não configuradas

**Solução**:

**Passo 1 - Verifique se o .env existe:**
```bash
ls -la .env
# Se não existir:
cp .env.example .env
nano .env  # edite e adicione credenciais
```

**Passo 2 - Verifique o conteúdo:**
```bash
cat .env
# Deve conter:
# AWS_ACCESS_KEY_ID=...
# AWS_SECRET_ACCESS_KEY=...
# AWS_SESSION_TOKEN=...  # Obrigatório no Learner Lab
```

**Passo 3 - Verifique se python-dotenv está instalado:**
```bash
pip install python-dotenv
```

**Passo 4 - Use o diagnóstico:**
```bash
cd src
python aws_config.py
```

---

### Erro: `The security token included in the request is invalid`

**Causa**: `AWS_SESSION_TOKEN` ausente ou inválido

**Solução**:

**No AWS Learner Lab, o session token é OBRIGATÓRIO!**

1. Acesse AWS Details no Learner Lab
2. Copie também a linha do `AWS_SESSION_TOKEN`
3. Adicione no arquivo `.env`:
   ```
   AWS_SESSION_TOKEN=FwoGZXIvYXdzEPj//////////...
   ```

---

### Erro: `An error occurred (ExpiredToken)`

**Causa**: Credenciais expiraram (comum no Learner Lab)

**Solução**:

**No Learner Lab:**
1. Clique em "Start Lab" novamente
2. Aguarde o indicador ficar verde
3. Clique em "AWS Details" → "Show"
4. Copie TODAS as três linhas novamente
5. Atualize o arquivo `.env`

**Conta AWS Regular:**
```bash
aws configure
# Digite novas credenciais
```

---

### Erro: `InvalidClientTokenId`

**Causa**: Access Key incorreta ou inválida

**Solução**:

1. Verifique se copiou a credencial completa (sem espaços extras)
2. Verifique se não há caracteres especiais corrompidos
3. Obtenha novas credenciais do AWS Console/Learner Lab
4. No Learner Lab, reinicie a sessão e copie novamente

---

### Erro: `SignatureDoesNotMatch`

**Causa**: Secret Access Key incorreta

**Solução**:

1. Verifique se copiou a secret key completa
2. Verifique se não há quebras de linha ou espaços
3. Obtenha novas credenciais
4. Certifique-se de que não há caracteres ocultos

---

## 🖼️ Problemas com o Rekognition

### Erro: `AccessDeniedException`

**Causa**: Falta de permissões IAM

**Solução**:

**No Learner Lab:**
- Verifique se o serviço Rekognition está disponível
- Alguns recursos podem estar bloqueados
- Use apenas operações básicas (detect_labels, detect_faces)

**Conta Regular:**
```bash
# Adicione política ao usuário IAM:
# AmazonRekognitionFullAccess
# ou crie política customizada com permissões específicas
```

---

### Erro: `InvalidImageFormatException`

**Causa**: Formato de imagem não suportado

**Solução**:

**Formatos suportados**: JPEG, PNG

**Conversão**:
```python
from PIL import Image

# Converte para JPEG
img = Image.open('imagem.webp')
img.convert('RGB').save('imagem.jpg', 'JPEG')
```

---

### Erro: `ImageTooLargeException`

**Causa**: Imagem muito grande (> 5MB para bytes)

**Solução**:

**Opção 1 - Reduzir tamanho:**
```python
from PIL import Image

img = Image.open('imagem.jpg')
img.thumbnail((1920, 1080))
img.save('imagem_reduzida.jpg', quality=85)
```

**Opção 2 - Usar S3:**
```python
# Upload para S3 primeiro
s3_client.upload_file('imagem_grande.jpg', 'meu-bucket', 'imagem.jpg')

# Usa referência S3
response = analyzer.detect_labels(
    s3_bucket='meu-bucket',
    s3_key='imagem.jpg'
)
```

---

### Erro: `InvalidS3ObjectException`

**Causa**: Objeto S3 não encontrado ou sem permissão

**Solução**:

1. Verifique se o bucket existe
2. Verifique se o objeto existe no bucket
3. Verifique permissões:
   ```python
   # O Rekognition precisa de permissão para ler do S3
   # Adicione política no bucket ou IAM role
   ```

---

### Erro: `ResourceNotFoundException`

**Causa**: Collection ou recurso não existe

**Solução**:

```python
# Crie a collection primeiro
rekognition_client.create_collection(CollectionId='minha-collection')

# Depois use-a
response = rekognition_client.index_faces(
    CollectionId='minha-collection',
    Image={'S3Object': {...}}
)
```

---

## 🎓 Problemas do AWS Learner Lab

### Problema: "Start Lab" não funciona

**Causas possíveis**:
1. Créditos esgotados
2. Sessão anterior não terminou
3. Problema temporário da AWS Academy

**Solução**:
1. Aguarde 5 minutos e tente novamente
2. Faça logout e login novamente
3. Limpe cache do navegador
4. Tente em modo anônimo/privado
5. Contate o suporte da AWS Academy se persistir

---

### Problema: Créditos acabaram

**Sintomas**:
- Não consegue iniciar o lab
- Mensagem de budget exceeded

**Solução**:
- Aguarde o reset mensal de créditos
- Use conta AWS regular (com cuidado nos custos)
- Otimize uso:
  - Teste com imagens pequenas
  - Limite número de chamadas
  - Use apenas o necessário

---

### Problema: Sessão expirou durante uso

**Sintomas**:
- Erro de credenciais após algumas horas
- ExpiredToken error

**Solução**:
1. Salve seu trabalho
2. Clique em "Start Lab" novamente
3. Atualize credenciais:
   ```bash
   # Copie novas credenciais
   nano .env  # Cole as novas
   ```
4. Continue trabalhando

---

### Problema: Rekognition não disponível no Learner Lab

**Verificação**:
```python
import boto3

client = boto3.client('rekognition', region_name='us-east-1')
try:
    # Tenta listar collections (operação básica)
    response = client.list_collections(MaxResults=1)
    print("✓ Rekognition disponível")
except Exception as e:
    print(f"✗ Erro: {e}")
```

**Se não disponível**:
- Documente com screenshots das tentativas
- Explique a limitação no README
- Use simulação/mock para demonstração

---

## 💻 Problemas de Execução

### Erro: `FileNotFoundError: [Errno 2] No such file or directory`

**Causa**: Caminho de arquivo incorreto

**Solução**:

```python
# Use caminho absoluto
from pathlib import Path

project_root = Path(__file__).parent.parent
image_path = project_root / 'examples' / 'imagem.jpg'

# ou caminho relativo correto
image_path = '../examples/imagem.jpg'
```

---

### Erro: `ImportError: cannot import name 'RekognitionAnalyzer'`

**Causa**: Módulo não encontrado ou erro de import

**Solução**:

```bash
# Verifique a estrutura
cd ir_alem_1
python -c "import sys; sys.path.insert(0, 'src'); from rekognition_analyzer import RekognitionAnalyzer; print('OK')"

# Se der erro, verifique:
ls -la src/__init__.py
ls -la src/rekognition_analyzer.py
```

---

### Erro: Hanging/travamento durante execução

**Causa**: Imagem muito grande ou rede lenta

**Solução**:

1. Use timeout:
   ```python
   import boto3
   from botocore.config import Config
   
   config = Config(
       connect_timeout=5,
       read_timeout=60
   )
   
   client = boto3.client('rekognition', config=config)
   ```

2. Reduza tamanho da imagem
3. Verifique conexão de rede

---

## 🚨 Erros Comuns da API

### `ThrottlingException`

**Causa**: Muitas requisições em pouco tempo

**Solução**:
```python
import time

# Adicione delay entre chamadas
for image in images:
    response = analyzer.detect_labels(image)
    time.sleep(0.5)  # Aguarda 500ms
```

---

### `ProvisionedThroughputExceededException`

**Causa**: Limite de taxa excedido

**Solução**:
```python
from botocore.exceptions import ClientError
import time

def retry_with_backoff(func, max_retries=3):
    for i in range(max_retries):
        try:
            return func()
        except ClientError as e:
            if e.response['Error']['Code'] == 'ProvisionedThroughputExceededException':
                wait_time = (2 ** i)  # Exponential backoff
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Max retries exceeded")
```

---

### `LimitExceededException`

**Causa**: Limite de quota da conta

**Solução**:
- Aguarde o reset do limite (geralmente 1 hora)
- Solicite aumento de quota via AWS Support
- No Learner Lab, use com moderação

---

## 🔍 Diagnóstico Geral

### Script de Diagnóstico Completo

Execute para diagnóstico completo:

```bash
cd src
python setup_check.py
```

### Verificação Manual

```python
# 1. Teste Python
python --version  # Deve ser 3.8+

# 2. Teste dependências
python -c "import boto3; print('boto3 OK')"
python -c "import PIL; print('Pillow OK')"

# 3. Teste credenciais
python -c "import os; print('AWS_ACCESS_KEY_ID' in os.environ)"

# 4. Teste Rekognition
python -c "import boto3; boto3.client('rekognition'); print('Client OK')"
```

---

## 📞 Ainda Precisa de Ajuda?

1. **Verifique a documentação**:
   - [README.md](README.md)
   - [QUICKSTART.md](QUICKSTART.md)

2. **Execute diagnósticos**:
   ```bash
   python src/setup_check.py
   python src/aws_config.py
   ```

3. **Revise exemplos**:
   - [example_usage.py](src/example_usage.py)
   - [rekognition_analyzer.py](src/rekognition_analyzer.py)

4. **Consulte documentação oficial**:
   - [AWS Rekognition Docs](https://docs.aws.amazon.com/rekognition/)
   - [boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

5. **Contate suporte**:
   - AWS Academy Support (para Learner Lab)
   - AWS Support (conta regular)
   - Fórum AWS

---

**Última atualização**: 2025-11-20
