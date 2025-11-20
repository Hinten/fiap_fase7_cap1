# Imagens de Exemplo

Este diretório deve conter imagens de exemplo para testar as funcionalidades do AWS Rekognition.

## 📁 Imagens Recomendadas

### 1. agricultural_field.jpg
**Propósito**: Testar detecção de elementos agrícolas

**Conteúdo sugerido**:
- Plantação ou campo cultivado
- Culturas visíveis (milho, soja, trigo, etc.)
- Solo, vegetação

**Onde encontrar**:
- Banco de imagens gratuitas (Unsplash, Pexels)
- Pesquisa: "agricultural field", "farm crops", "plantation"

---

### 2. security_camera.jpg
**Propósito**: Testar detecção de pessoas e objetos de segurança

**Conteúdo sugerido**:
- Pessoas em um ambiente
- Objetos como portas, janelas
- Veículos (opcional)

**Onde encontrar**:
- Bancos de imagens de segurança
- Pesquisa: "people in room", "security camera view"

---

### 3. document.jpg
**Propósito**: Testar OCR (extração de texto)

**Conteúdo sugerido**:
- Documento com texto legível
- Placa de veículo
- Letreiro
- Formulário

**Onde encontrar**:
- Tire foto de um documento próprio
- Use documento de exemplo (sem informações sensíveis)
- Pesquisa: "sample document", "text sign"

---

### 4. content_check.jpg
**Propósito**: Testar moderação de conteúdo

**Conteúdo sugerido**:
- Imagem neutra e apropriada para teste
- Foto familiar
- Paisagem

**Nota**: Para este teste, use imagens apropriadas

---

### 5. face1.jpg e face2.jpg
**Propósito**: Testar comparação de rostos

**Conteúdo sugerido**:
- face1.jpg: Rosto de uma pessoa (foto 1)
- face2.jpg: Mesmo rosto em outra foto ou rosto diferente

**Onde encontrar**:
- Use suas próprias fotos
- Banco de imagens com rostos autorizados
- Pesquisa: "face portrait", "person headshot"

---

## ⚠️ Avisos Importantes

### Direitos Autorais
- Use apenas imagens que você tem direito de usar
- Prefira bancos de imagens com licença livre (CC0, Unsplash License)
- Não use imagens protegidas por copyright sem permissão

### Privacidade
- Não use fotos de terceiros sem permissão
- Evite imagens com informações pessoais identificáveis
- Considere implicações de privacidade ao compartilhar

### Tamanho de Arquivo
- Rekognition aceita até 5MB por imagem (via bytes)
- Sem limite para imagens no S3
- Recomendado: < 2MB para testes rápidos

### Formatos Suportados
- JPEG (recomendado)
- PNG
- Resolução mínima: 80 pixels (menor dimensão)
- Resolução máxima: 15360 pixels (qualquer dimensão)

---

## 🌐 Fontes de Imagens Gratuitas

### Bancos de Imagens CC0 (Domínio Público)
- [Unsplash](https://unsplash.com/) - Fotos de alta qualidade
- [Pexels](https://www.pexels.com/) - Fotos e vídeos gratuitos
- [Pixabay](https://pixabay.com/) - Imagens e vetores
- [StockSnap](https://stocksnap.io/) - Fotos livres de direitos

### Imagens Agrícolas
- [USDA Photo Gallery](https://www.usda.gov/media/photo-gallery)
- [Wikimedia Commons - Agriculture](https://commons.wikimedia.org/wiki/Category:Agriculture)

### Imagens de Teste AWS
- [AWS Rekognition Sample Images](https://github.com/aws-samples/amazon-rekognition-code-samples)

---

## 📝 Como Adicionar Imagens

1. Baixe ou tire as fotos necessárias
2. Renomeie conforme a lista acima
3. Coloque neste diretório (`examples/`)
4. Execute os testes:

```bash
cd src
python example_usage.py
```

---

## 🔍 Teste Sem Imagens

Se você não tiver imagens agora, pode testar apenas a configuração:

```bash
cd src
python setup_check.py
```

Este script verifica se tudo está configurado corretamente sem fazer chamadas à API.

---

## 📊 Características Ideais por Tipo

### Para Detecção de Labels
- Boa iluminação
- Objetos bem definidos
- Resolução adequada (mínimo 1024x768)
- Foco nítido

### Para Detecção Facial
- Rosto visível e frontal
- Boa iluminação
- Resolução mínima 80x80 pixels para o rosto
- Sem obstruções (mãos, cabelo cobrindo)

### Para OCR (Texto)
- Texto legível
- Contraste alto entre texto e fundo
- Texto horizontal (melhor precisão)
- Boa resolução

---

**Última atualização**: 2025-11-20
