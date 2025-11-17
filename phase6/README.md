# Fase 6: Visão Computacional com Redes Neurais

## 📋 Descrição

Sistema de visão computacional com YOLO para monitoramento visual da saúde das plantações.

## 🎯 Objetivos

- Detecção de pragas e insetos
- Identificação de doenças em plantas
- Monitoramento de crescimento irregular
- Detecção de deficiências nutricionais
- Processamento de imagens estáticas
- Integração com ESP32-CAM (opcional)

## 📂 Estrutura

```
phase6/
├── modelo_yolo/    # Pesos e configuração do modelo
├── inferencia/     # Scripts de inferência
└── images/         # Imagens estáticas para processamento
```

## 👁️ Modelo YOLO

### Versão
- **YOLOv8** (recomendado) ou YOLOv5
- **Tipo**: Object Detection
- **Framework**: Ultralytics / PyTorch

### Classes Detectadas

1. **Pragas**
   - Lagarta
   - Pulgão
   - Mosca-branca
   - Percevejo

2. **Doenças**
   - Ferrugem
   - Mancha-foliar
   - Míldio
   - Oídio

3. **Outros**
   - Crescimento irregular
   - Deficiência nutricional
   - Descoloração foliar

### Métricas do Modelo
- **Precisão (Precision)**: 85%+
- **Recall**: 80%+
- **mAP@0.5**: 82%+
- **Confiança mínima**: 0.5

## 🔧 Como Usar

### Inferência em Imagens

```bash
cd phase6/inferencia
python detect.py --source ../images/ --conf 0.5
```

### Inferência em Vídeo

```bash
python detect.py --source video.mp4 --conf 0.5
```

### Inferência em Webcam/ESP32-CAM

```bash
python detect.py --source 0  # Webcam
python detect.py --source http://192.168.1.100:81/stream  # ESP32-CAM
```

### Via Python Script

```python
from ultralytics import YOLO
from PIL import Image

# Carregar modelo
modelo = YOLO('../modelo_yolo/best.pt')

# Fazer inferência
resultados = modelo.predict(
    source='../images/planta.jpg',
    conf=0.5,
    save=True
)

# Processar resultados
for r in resultados:
    for box in r.boxes:
        classe = int(box.cls[0])
        confianca = float(box.conf[0])
        bbox = box.xyxy[0].tolist()
        
        print(f"Detectado: {modelo.names[classe]}")
        print(f"Confiança: {confianca:.2f}")
        print(f"Bounding Box: {bbox}")
```

## 📸 ESP32-CAM (Opcional)

### Setup Hardware
1. Conectar ESP32-CAM à rede WiFi
2. Configurar stream de vídeo
3. Obter endereço IP
4. Testar acesso via navegador: `http://IP:81/stream`

### Integração com Sistema

```python
import requests
from PIL import Image
from io import BytesIO

# Capturar frame
response = requests.get('http://192.168.1.100:81/capture')
imagem = Image.open(BytesIO(response.content))

# Processar com YOLO
resultados = modelo.predict(source=imagem)
```

## 🎯 Pipeline de Processamento

1. **Captura**: Imagem via upload ou ESP32-CAM
2. **Pré-processamento**: Resize, normalização
3. **Inferência**: Detecção com YOLO
4. **Pós-processamento**: NMS, threshold
5. **Análise**: Identificar alertas críticos
6. **Ação**: Enviar alertas se necessário

## 📊 Exemplo de Output

```json
{
  "imagem": "planta_001.jpg",
  "timestamp": "2024-01-15T14:30:00",
  "deteccoes": [
    {
      "classe": "lagarta",
      "confianca": 0.87,
      "bbox": [120, 45, 180, 95],
      "severidade": "CRITICAL"
    },
    {
      "classe": "mancha_foliar",
      "confianca": 0.72,
      "bbox": [200, 150, 280, 210],
      "severidade": "WARNING"
    }
  ],
  "alerta_enviado": true
}
```

## 🚨 Integração com Sistema de Alertas

Quando detectada uma praga ou doença crítica:

```python
if confianca > 0.7 and classe in ['praga', 'doenca']:
    enviar_alerta({
        'tipo': 'Praga Detectada',
        'mensagem': f'{modelo.names[classe]} detectado com {confianca:.0%} de confiança',
        'severidade': 'CRITICAL',
        'setor': 'Setor A',
        'imagem': 'path/to/imagem.jpg'
    })
```

## 📦 Dependências Específicas

```
torch
torchvision
ultralytics
opencv-python
pillow
```

## 🔗 Repositório Original

[fiap_fase6_cap1](https://github.com/Hinten/fiap_fase6_cap1)

## 📝 O Que Trazer do Repositório Original

- Modelo YOLO treinado (best.pt)
- Scripts de inferência
- Dataset de imagens de exemplo
- Labels/classes (classes.txt)
- Código de treinamento (se disponível)
- Integração ESP32-CAM (se implementado)
- Notebooks de análise

## 🎓 Treinamento do Modelo (Referência)

Se precisar retreinar o modelo:

```bash
# Preparar dataset no formato YOLO
# dataset/
#   ├── images/
#   │   ├── train/
#   │   └── val/
#   └── labels/
#       ├── train/
#       └── val/

# Treinar
yolo detect train \
  data=dataset.yaml \
  model=yolov8n.pt \
  epochs=100 \
  imgsz=640 \
  batch=16
```
