# 🚀 Guia Rápido de Início

Este guia fornece instruções passo a passo para começar a usar o projeto AWS Rekognition.

---

## ⏱️ Início Rápido (5 minutos)

### 1. Clone o Repositório
```bash
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1/ir_alem_1
```

### 2. Instale as Dependências
```bash
# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configure as Credenciais AWS

#### Opção A: AWS Learner Lab

1. Acesse o AWS Learner Lab
2. Clique em "Start Lab"
3. Clique em "AWS Details" → "Show" (ao lado de AWS CLI)
4. Copie as três linhas de credenciais
5. Crie o arquivo `.env`:

```bash
cp .env.example .env
nano .env  # Cole as credenciais copiadas
```

#### Opção B: Configuração Interativa

```bash
cd src
python aws_config.py --setup
```

### 4. Verifique a Configuração
```bash
cd src
python setup_check.py
```

Se tudo estiver verde (✓), você está pronto!

### 5. Execute o Primeiro Teste
```bash
cd src
python example_usage.py
```

---

## 📖 Passos Detalhados

### Passo 1: Preparação do Ambiente

#### 1.1. Verifique o Python
```bash
python --version
# Deve ser Python 3.8 ou superior
```

#### 1.2. Crie o Ambiente Virtual
```bash
python -m venv venv
```

**Por que usar ambiente virtual?**
- Isola as dependências do projeto
- Evita conflitos com outros projetos
- Facilita a reprodução do ambiente

#### 1.3. Ative o Ambiente Virtual

**Linux/Mac:**
```bash
source venv/bin/activate
# Você verá (venv) no início da linha
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

#### 1.4. Instale as Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Passo 2: Configuração AWS

#### 2.1. Acesse o AWS Learner Lab

1. Faça login no AWS Academy
2. Acesse seu curso
3. Clique em "Learner Lab - Foundational Services"

#### 2.2. Inicie o Ambiente

1. Clique no botão **"Start Lab"**
2. Aguarde o indicador mudar de vermelho para verde
3. Isso pode levar 1-2 minutos

#### 2.3. Obtenha as Credenciais

1. Clique em **"AWS Details"**
2. Na seção "AWS CLI", clique em **"Show"**
3. Você verá três linhas:
   ```
   export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/...
   export AWS_SESSION_TOKEN=FwoGZXIvYXdzEPj//////////...
   ```

#### 2.4. Configure no Projeto

**Método 1: Arquivo .env (Recomendado)**

1. Copie o arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env`:
   ```bash
   nano .env  # ou use seu editor preferido
   ```

3. Cole as credenciais (sem o "export"):
   ```
   AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/...
   AWS_SESSION_TOKEN=FwoGZXIvYXdzEPj//////////...
   AWS_DEFAULT_REGION=us-east-1
   ```

**Método 2: Variáveis de Ambiente**

Cole diretamente no terminal (temporário):
```bash
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/...
export AWS_SESSION_TOKEN=FwoGZXIvYXdzEPj//////////...
export AWS_DEFAULT_REGION=us-east-1
```

---

### Passo 3: Verificação

#### 3.1. Execute o Script de Verificação
```bash
cd src
python setup_check.py
```

#### 3.2. Interpretando os Resultados

**Tudo OK (✓✓✓✓✓):**
```
✓ Versão do Python
✓ Dependências
✓ Credenciais AWS
✓ Acesso ao Rekognition
✓ Estrutura de Diretórios
```

**Problemas comuns:**

**✗ Dependências não instaladas:**
```bash
pip install -r requirements.txt
```

**✗ Credenciais não configuradas:**
- Verifique se o arquivo `.env` existe
- Verifique se as credenciais estão corretas
- Verifique se incluiu o AWS_SESSION_TOKEN

**✗ Python desatualizado:**
- Instale Python 3.8 ou superior
- Use `python3` em vez de `python` se necessário

---

### Passo 4: Primeiro Uso

#### 4.1. Prepare Imagens de Teste

Adicione imagens na pasta `examples/`:
- `agricultural_field.jpg` - Para análise agrícola
- `security_camera.jpg` - Para detecção de pessoas
- `document.jpg` - Para extração de texto
- `face1.jpg` e `face2.jpg` - Para comparação

**Fontes de imagens:**
- [Unsplash](https://unsplash.com/)
- [Pexels](https://www.pexels.com/)
- Suas próprias fotos

#### 4.2. Execute os Exemplos

```bash
cd src
python example_usage.py
```

#### 4.3. Menu Interativo

O script apresentará um menu:
```
1. Análise Agrícola
2. Análise de Segurança
3. Extração de Texto (OCR)
4. Moderação de Conteúdo
5. Comparação de Rostos
0. Sair
```

Escolha uma opção e forneça o caminho da imagem quando solicitado.

---

### Passo 5: Uso Programático

#### 5.1. Código Básico

Crie um arquivo `meu_teste.py`:

```python
from rekognition_analyzer import RekognitionAnalyzer

# Inicializa o analisador
analyzer = RekognitionAnalyzer(region_name='us-east-1')

# Analisa uma imagem
response = analyzer.detect_labels(
    image_path='../examples/sua_imagem.jpg',
    max_labels=10,
    min_confidence=80.0
)

# Exibe resultados formatados
print(analyzer.format_labels_output(response))
```

#### 5.2. Execute
```bash
cd src
python meu_teste.py
```

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'boto3'"
**Solução:**
```bash
pip install boto3
# ou
pip install -r requirements.txt
```

### Erro: "Unable to locate credentials"
**Solução:**
1. Verifique se o arquivo `.env` existe
2. Verifique se as variáveis estão corretas
3. Tente executar `python src/aws_config.py` para diagnóstico

### Erro: "An error occurred (InvalidClientTokenId)"
**Solução:**
- Suas credenciais expiraram
- No Learner Lab, copie novas credenciais
- Atualize o arquivo `.env`

### Erro: "Session token expired"
**Solução:**
- No Learner Lab, as sessões expiram após 4 horas
- Clique em "Start Lab" novamente
- Copie novas credenciais

### Erro: "Service Rekognition not available"
**Solução:**
- Verifique se está usando a região correta (us-east-1)
- Verifique se o serviço está disponível no Learner Lab
- Tente no console AWS primeiro

---

## 📊 Próximos Passos

### 1. Documente com Screenshots
- Tire prints do console AWS
- Salve em `docs/screenshots/`
- Siga o guia em `docs/screenshots/README.md`

### 2. Crie Casos de Uso Personalizados
- Adapte os exemplos para seu contexto
- Teste com suas próprias imagens
- Documente os resultados

### 3. Grave o Vídeo Demonstrativo
- Use o roteiro em `video_script.md`
- Mostre o código funcionando
- Explique as configurações AWS
- Máximo 5 minutos

### 4. Otimize para Seu Caso de Uso
- Ajuste parâmetros (`min_confidence`, `max_labels`)
- Adicione filtros específicos
- Integre com outros sistemas

---

## 💡 Dicas

### Economize Créditos
- Use imagens pequenas (< 1MB)
- Faça poucos testes inicialmente
- Use `setup_check.py` que não faz chamadas à API

### Segurança
- Nunca commite o arquivo `.env`
- Use `.gitignore` para proteger credenciais
- Revogue credenciais se comprometidas

### Performance
- Imagens menores processam mais rápido
- Use S3 para imagens grandes (> 5MB)
- Cache resultados quando possível

### Debugging
- Ative logging detalhado
- Use `min_confidence` menor para mais resultados
- Verifique a documentação da API

---

## 📚 Recursos Adicionais

- [Documentação AWS Rekognition](https://docs.aws.amazon.com/rekognition/)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS Learner Lab Guide](https://awsacademy.instructure.com/)
- [README Principal](README.md)

---

## 🆘 Precisa de Ajuda?

1. Consulte o [README completo](README.md)
2. Verifique a [documentação dos screenshots](docs/screenshots/README.md)
3. Execute `python src/setup_check.py` para diagnóstico
4. Revise os exemplos em `src/example_usage.py`

---

**Última atualização**: 2025-11-20
