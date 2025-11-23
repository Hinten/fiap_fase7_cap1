# Modelos YOLO Treinados

Este diretório é destinado ao armazenamento de modelos YOLO treinados (arquivos `.pt`).

## Como Usar

1. **Treine seu modelo** usando os notebooks em `src/modelo_yolo/`:
   - `yolo_padrao_fiap.ipynb` - Treinamento com YOLO padrão
   - `yolo7.ipynb` - Treinamento com YOLOv7
   - `CNN.ipynb` - Treinamento com CNN

2. **Salve o modelo treinado** (arquivo `.pt`) neste diretório

3. **Acesse o Dashboard** e navegue até "Inferência YOLO" no menu

4. **Selecione o modelo** e faça upload de imagens para análise

## Formato dos Modelos

- **Extensão:** `.pt` (PyTorch)
- **Framework:** Ultralytics YOLO (YOLOv5/YOLOv8)
- **Conteúdo:** Pesos do modelo treinado + metadados

## Exemplo de Estrutura

```
modelos_treinados/
├── best.pt                 # Melhor modelo do treinamento
├── yolo_bananas_v1.pt     # Modelo para detecção de bananas
├── yolo_frutas_final.pt   # Modelo final de frutas
└── README.md              # Este arquivo
```

## Upload de Modelos pelo Dashboard

Você também pode fazer upload de modelos diretamente pelo dashboard na página "Inferência YOLO".

## Notas Importantes

- Modelos grandes (>100MB) podem demorar para carregar
- O primeiro carregamento pode ser mais lento (criação de cache)
- Modelos em cache são reutilizados para melhor performance
