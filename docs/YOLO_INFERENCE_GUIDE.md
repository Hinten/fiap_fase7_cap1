# YOLO Model Inference - Usage Guide

## Overview
This guide demonstrates how to use the YOLO Model Inference feature in the FarmTech Solutions dashboard.

## Features Implemented

### 1. Model Management
- **Model Selection**: Dropdown to select from available trained models in `src/modelo_yolo/modelos_treinados/`
- **Model Upload**: Direct upload of `.pt` model files through the dashboard
- **Model Information**: Display of model name and file size

### 2. Image Upload and Preview
- **Supported Formats**: JPG, JPEG, PNG, BMP
- **Image Preview**: Side-by-side display of original and processed images
- **Drag-and-drop**: Easy file upload interface

### 3. Detection Configuration
- **Confidence Threshold**: Adjustable slider (0.0 - 1.0, default: 0.25)
  - Controls minimum confidence for accepting detections
- **IoU Threshold**: Adjustable slider (0.0 - 1.0, default: 0.45)
  - Controls Non-Maximum Suppression for overlapping detections
- **Max Detections**: Number input (1 - 1000, default: 300)
  - Limits maximum objects detected per image

### 4. Results Visualization
- **Annotated Image**: Bounding boxes with class labels and confidence scores
- **Detection Metrics**:
  - Total detections count
  - Average confidence
  - Maximum confidence
- **Detailed Table**: Lists all detections with:
  - Class/category
  - Confidence percentage
  - Bounding box coordinates (x1, y1, x2, y2)

### 5. Export Functionality
- **Download Button**: Save annotated images as PNG
- **Preserved Filename**: Original filename with "deteccoes_" prefix
- **High Quality**: PNG format with full resolution

## User Interface Layout

```
┌─────────────────────────────────────────────────────────────┐
│ 🎯 Inferência com Modelos YOLO                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 1️⃣ Selecionar Modelo                                        │
│ ┌──────────────────────────┬─────────────────┐             │
│ │ [Dropdown: yolo_model.pt]│ [Upload Button] │             │
│ │ 📦 Modelo: yolo_model.pt │                 │             │
│ │ 💾 Tamanho: 6.1 MB       │                 │             │
│ └──────────────────────────┴─────────────────┘             │
│                                                             │
│ 2️⃣ Selecionar Imagem                                        │
│ ┌─────────────────────────────────────────────┐             │
│ │ [Upload de Imagem: JPG, JPEG, PNG, BMP]    │             │
│ └─────────────────────────────────────────────┘             │
│                                                             │
│ ┌──────────────────────┬──────────────────────┐             │
│ │ 📷 Imagem Original   │ 🎯 Detecções         │             │
│ │ [Image Preview]      │ [Annotated Image]    │             │
│ └──────────────────────┴──────────────────────┘             │
│                                                             │
│ 3️⃣ Configurações de Detecção                                │
│ ┌────────────┬────────────┬──────────────────┐             │
│ │ Confiança  │ IoU (NMS)  │ Detecções Máx    │             │
│ │ [0.25 ◄━━━►│[0.45 ◄━━━►]│ [300]            │             │
│ └────────────┴────────────┴──────────────────┘             │
│                                                             │
│ 4️⃣ Realizar Detecção                                        │
│ ┌─────────────────────────────────────────────┐             │
│ │      🚀 Detectar Objetos [BUTTON]           │             │
│ └─────────────────────────────────────────────┘             │
│                                                             │
│ 📊 Resultados da Detecção                                   │
│ ┌──────────┬───────────────┬────────────────┐              │
│ │ Total: 3 │ Conf Média:   │ Conf Máxima:   │              │
│ │          │ 87.5%         │ 95.2%          │              │
│ └──────────┴───────────────┴────────────────┘              │
│                                                             │
│ 🔍 Detalhes das Detecções                                   │
│ ┌───────────────────────────────────────────────────────┐   │
│ │ #  │ Classe  │ Confiança │ Coordenadas (x,y,x,y)    │   │
│ ├────┼─────────┼───────────┼──────────────────────────┤   │
│ │ 1  │ Banana  │ 95.2%     │ (100, 100, 250, 200)     │   │
│ │ 2  │ Apple   │ 87.3%     │ (400, 150, 550, 300)     │   │
│ │ 3  │ Leaf    │ 80.1%     │ (150, 300, 300, 400)     │   │
│ └────┴─────────┴───────────┴──────────────────────────┘   │
│                                                             │
│ 💾 Download                                                 │
│ ┌─────────────────────────────────────────────┐             │
│ │   📥 Baixar Imagem com Detecções [BUTTON]   │             │
│ └─────────────────────────────────────────────┘             │
└─────────────────────────────────────────────────────────────┘
```

## Menu Navigation

The YOLO inference feature is accessible through the sidebar menu:

```
Sidebar Menu:
├── 🏠 Principal
├── Cadastro de Sensores
│   ├── Sensores
│   ├── Leituras
│   └── ...
├── 📊 Gráficos
│   ├── Todas as Leituras
│   ├── Umidade
│   └── ...
├── 🌤 Clima
│   ├── Previsão do Tempo
│   └── Irrigação
├── 🔮 Modelo Preditivo
│   ├── Exploração de Dados
│   └── Previsão Manual
├── 🎯 Modelo YOLO          ← NEW SECTION
│   └── Inferência YOLO     ← NEW PAGE
├── 🔔 Notificações
└── 📥 Exportar/Importar
```

## Testing the Feature

### Without a Trained Model

1. Start the dashboard: `streamlit run main_dash.py`
2. Navigate to "Modelo YOLO" → "Inferência YOLO"
3. You'll see a warning: "Nenhum modelo encontrado"
4. Use the upload button to add a `.pt` model file
5. After upload, refresh the page to see the model in the list

### With a Trained Model

1. Place your trained model (e.g., `best.pt`) in `src/modelo_yolo/modelos_treinados/`
2. Start the dashboard
3. Navigate to "Inferência YOLO"
4. Select your model from the dropdown
5. Upload an image (JPG, PNG, etc.)
6. Adjust detection parameters if needed
7. Click "🚀 Detectar Objetos"
8. View results and download annotated image

## Implementation Status

✅ **Completed Features:**
- Model loading and caching system
- File upload and validation
- Image preprocessing and display
- YOLO inference integration
- Results visualization with bounding boxes
- Confidence and IoU configuration
- Detection metrics calculation
- Detailed detection table
- Download functionality
- Error handling and user feedback
- Integration with dashboard navigation
- Comprehensive documentation

✅ **Code Quality:**
- Modular architecture
- Type hints
- Error handling
- Logging support
- Cache optimization
- Memory efficient

✅ **Documentation:**
- README.md comprehensive guide
- In-code docstrings
- Usage examples
- Troubleshooting section
- Model directory README

## Technical Details

### Model Loader (`src/modelo_yolo/model_loader.py`)
- Singleton cache pattern for loaded models
- Lazy loading strategy
- Memory-efficient model management
- Error handling for corrupted files
- Model information extraction

### Inference View (`src/dashboard/modelo_yolo/inference_view.py`)
- Streamlit page implementation
- Real-time parameter adjustment
- Image processing with PIL and OpenCV
- Result parsing and visualization
- Download generation

### Integration Points
- `src/dashboard/menu.py`: Sidebar menu entry
- `src/dashboard/navigator.py`: Page routing
- `requirements.txt`: Dependencies added

## Future Enhancements (Optional)

Potential improvements for future versions:
- Batch image processing
- Video inference support
- Model performance comparison
- Export results as JSON/CSV
- Real-time webcam inference
- Custom class name mapping
- Model training interface
- Dataset annotation tools

## Notes

- First model load may take 10-30 seconds depending on size
- Subsequent loads are faster due to caching
- GPU acceleration is used if available (CUDA)
- Models are kept in memory during session
- Large images are processed efficiently
- All operations are logged for debugging
