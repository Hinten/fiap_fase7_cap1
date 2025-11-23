# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# fiap_fase6_cap1

## Atividade em Grupo: FIAP - 1TIAOB - 2025/1 - Fase6 Cap 1

## 👨‍🎓 Integrantes: 
- <a href="">Alice C. M. Assis - RM 566233</a>
- <a href="">Leonardo S. Souza - RM 563928</a>
- <a href="">Lucas B. Francelino - RM 561409</a> 
- <a href="">Pedro L. T. Silva - RM 561644</a> 
- <a href="">Vitor A. Bezerra - RM 563001</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="proflucas.moreira@fiap.com.br">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="profandre.chiovato@fiap.com.br">André Godoi Chiovato</a>


## 📜 Descrição rápida do projeto

Neste repositório apresentamos a entrega da Fase 6 — desenvolvimento e avaliação de modelos de Visão Computacional usando YOLO e abordagens concorrentes. O objetivo principal é montar um dataset customizado com duas classes (A e B), treinar e validar um detector baseado em YOLO, comparar com outras abordagens (YOLO padrão e uma CNN treinada do zero) e documentar resultados, conclusões e limitações.

O projeto também oferece duas opções opcionais ("Ir Além") para implementação extra: (1) integração com ESP32-CAM para captura e inferência em tempo real e (2) aplicações de Transfer Learning + Fine Tuning com segmentação prévia do objeto.

# URL do dataset no Google Drive

- Link para o dataset no Google Drive (pasta principal): <https://drive.google.com/drive/u/1/folders/10XPnZK4l3INy824b0p2vtt5Od0s9g6n8>

## Links dos Notebooks e Vídeo Demonstrativo

- **Entrega 1**: [yolo_padrao_fiap.ipynb](src/entrega_1/yolo_padrao_fiap.ipynb)
- **Entrega 2**: 
  - [yolo7.ipynb](src/entrega_2/yolo7.ipynb)
  - [CNN.ipynb](src/entrega_2/CNN.ipynb)
- **Ir Além 1**:
  - [yolo_padrao_fiap_esp32cam.ipynb](src/ir_alem_2/criar_dataset_segmentado.ipynb)
- **Ir Além 2**:
  - [criar_dataset_segmentado.ipynb](src/ir_alem_2/criar_dataset_segmentado.ipynb)
  - [cnn_inicial_sem_crop.ipynb](src/ir_alem_2/cnn_inicial_sem_crop.ipynb)
  - [cnn_inicial_com_crop.ipynb](src/ir_alem_2/cnn_inicial_com_crop.ipynb)
  - [fine_tuning.ipynb](src/ir_alem_2/fine_tuning.ipynb)
  - [transfer_learning.ipynb](src/ir_alem_2/transfer_learning.ipynb)
- **Vídeos Demonstrativos**:
    - [Vídeo entrega 1](https://www.youtube.com/watch?v=ncGp6qdZ968)
    - [Vídeo entrega 2](https://youtu.be/CGsucOPqCpY)
    - [Vídeo Ir Além 1](https://youtu.be/StURW4G3Hww)
    - [Vídeo Ir Além 2](https://youtu.be/dfWgIeiQotM)

# Entrega 1

## Resumo da implementação 

### [https://www.youtube.com/watch?v=ncGp6qdZ968](https://www.youtube.com/watch?v=ncGp6qdZ968)

[yolo_padrao_fiap.ipynb](src/entrega_1/yolo_padrao_fiap.ipynb)

Neste notebook foi utilizada a linha do tempo abaixo para treinar e avaliar um detector YOLO na base criada em Google Drive.

Fluxo executado:
- Montagem do Google Drive (Colab):
  - from google.colab import drive; drive.mount('/content/drive')
- Definição de caminhos principais:
  - `DATASET_PATH = "/content/drive/MyDrive/FASE6_CAP1/yolo/data.yaml"` (arquivo YAML com paths do dataset e classes)
  - `teste_path = "/content/drive/MyDrive/FASE6_CAP1/yolo/test"` (pasta com imagens de teste)
- Preparação do ambiente:
  - Clone do repositório YOLO (quando necessário) e instalação de dependências.
- Modelo usado:
  - `ultralytics` YOLOv8 (pesos iniciais: `yolov8s.pt`).

Hiperparâmetros de treino (conforme notebook):
- epochs: 150 (o notebook configurou 150; o treinamento pode apresentar EarlyStopping dependendo do `patience`)
- imgsz: 640
- batch: 16
- patience: 30
- workers: 8
- device: 0
- seed: 42

Comando de treino (exemplo usado no notebook):
- model.train(data=DATASET_PATH, epochs=150, imgsz=640, batch=16, patience=30, workers=8, device=0, seed=42)

Inferência / geração de resultados:
- Previsões:
  - Ajustes: conf=0.65, iou=0.5, max_det=50
  - Salvamento: `save=True`, `save_txt=True`, `save_conf=True`
  - Projeto / pasta de saída (exemplo):
    - project: `/content/drive/MyDrive/FASE6_CAP1/yolo/outputs`
    - name: `banana_maca` (nome da execução)
- Resultado final informado no notebook: "Arquivos salvos em: /content/drive/MyDrive/FASE6_CAP1/yolo/outputs/banana_maca"

## Avaliação (síntese retirada do próprio notebook)
- Facilidade de uso / integração: fluxo simples usando a API `ultralytics` (YOLOv5) — rápida integração no Colab com Drive.
- Precisão: o notebook relata boa detecção para a classe `maca` com recall satisfatório em execuções iniciais.
- Tempo de treinamento: o autor notou que o modelo encerrou via EarlyStopping por volta de ~35 épocas em uma execução, embora o treino estivesse configurado para até 150 épocas.
- Tempo de inferência: aproximadamente 41,8 ms por imagem (valor reportado no notebook como exemplo de medição).

## Como reproduzir (passo a passo mínimo no Colab)
1. Abrir o notebook `src/entrega_1/yolo_padrao_fiap.ipynb` no Colab (ou copiar o conteúdo para um novo notebook no Drive).
2. Montar o Drive: `from google.colab import drive; drive.mount('/content/drive')`.
3. Verificar que `DATASET_PATH` e `teste_path` apontam para sua pasta no Drive (ex.: `/content/drive/MyDrive/FASE6_CAP1/yolo/`).
4. Instalar/rodar YOLO (se for usar o repositório local): `!git clone https://github.com/ultralytics/yolov5` e instalar requisitos; ou usar a API `ultralytics` (já presente no notebook).
5. Executar células de treino com os hiperparâmetros desejados (sugestão: testar 30 e 60 épocas como comparativo exigido no enunciado).
6. Rodar a célula de inferência e verificar os resultados salvos em `.../yolo/outputs/<nome_execucao>`.

## Arquivos gerados e local de salvamento
- Checkpoints e pesos: quando salvos pelo YOLO, ficam no diretório padrão do framework (ou no Drive, dependendo da configuração).
- Imagens de teste com detecções: `/content/drive/MyDrive/FASE6_CAP1/yolo/outputs/<nome_execucao>`
- Arquivos de texto com predições: salvos junto às imagens se `save_txt=True`.

## Observações e recomendações
- Ajuste `DATASET_PATH` no YAML para garantir que os paths de `train`, `val` e `test` estejam corretos antes de treinar.
- Se quiser reproduzir localmente, adapte os caminhos para o seu sistema e verifique compatibilidade de GPU (device index).
- Recomenda-se executar pelo menos duas sessões de treino com épocas bem diferentes (ex.: 30 e 60) para comparar métricas conforme requisito da Entrega 1.

# Entrega 2

## Resumo da implementação 

### [https://youtu.be/CGsucOPqCpY](https://youtu.be/CGsucOPqCpY)

[yolo7.ipynb](src/entrega_2/yolo7.ipynb)

Neste notebook foi utilizada a linha do tempo abaixo para treinar e avaliar um detector YOLOv7 na base criada em Google Drive.

Fluxo executado:
- Montagem do Google Drive (Colab):
  - from google.colab import drive; drive.mount('/content/drive')
- Definição de caminhos principais:
  - `DATASET_PATH = "/content/drive/MyDrive/FASE6_CAP1/yolo/data.yaml"` (arquivo YAML com paths do dataset e classes)
  - `teste_path = "/content/drive/MyDrive/FASE6_CAP1/yolo/test"` (pasta com imagens de teste)
- Preparação do ambiente:
  - Clone do repositório YOLOv7 e instalação de dependências.
- Modelo usado:
  - YOLOv7 (pesos iniciais: `yolov7.pt`).

Hiperparâmetros de treino (conforme notebook):
- epochs: 150
- batch-size: 16
- img: 640
- device: 0

Comando de treino (exemplo usado no notebook):
- python train.py --weights yolov7.pt --data $DATASET_PATH --epochs 150 --batch-size 16 --img 640 --device 0

Inferência / geração de resultados:
- Previsões:
  - Após treinamento, usar detect.py para inferência.
  - Exemplo: python detect.py --weights runs/train/exp/weights/best.pt --source $teste_path --img 640
- Resultado final informado no notebook: Similar ao YOLO padrão, com arquivos salvos em diretório de saída.

## Avaliação (síntese retirada do próprio notebook)
- Facilidade de uso / integração: O uso foi bastante simples e direto, com pipeline de treinamento e inferência pronto, dispensando definição manual de camadas ou arquitetura.
- Precisão: O modelo apresentou evolução rápida nas primeiras épocas, atingindo melhor desempenho na época 5, com possível instabilidade em épocas posteriores devido à falta de early stopping.
- Tempo de treinamento: O treinamento completo levou 35 épocas (~0,053 horas) até EarlyStopping.
- Tempo de inferência: A inferência foi rápida, com detecção em aproximadamente 41,8 ms por imagem.

## Como reproduzir (passo a passo mínimo no Colab)
1. Abrir o notebook `src/entrega_2/yolo7.ipynb` no Colab (ou copiar o conteúdo para um novo notebook no Drive).
2. Montar o Drive: `from google.colab import drive; drive.mount('/content/drive')`.
3. Verificar que `DATASET_PATH` e `teste_path` apontam para sua pasta no Drive (ex.: `/content/drive/MyDrive/FASE6_CAP1/yolo/`).
4. Clonar e instalar YOLOv7: `!git clone https://github.com/WongKinYiu/yolov7` e `!pip install -r requirements.txt`.
5. Executar treinamento: `!python train.py --weights yolov7.pt --data $DATASET_PATH --epochs 150 --batch-size 16 --img 640 --device 0`.
6. Para inferência: `!python detect.py --weights runs/train/exp/weights/best.pt --source $teste_path --img 640` e verificar resultados.

## Arquivos gerados e local de salvamento
- Checkpoints e pesos: Salvos em runs/train/exp/weights/.
- Imagens de teste com detecções: Salvas em runs/detect/exp/.
- Arquivos de texto com predições: Gerados junto às imagens.

## Observações e recomendações
- Ajuste `DATASET_PATH` no YAML para garantir que os paths estejam corretos.
- Para reproduzir localmente, adapte caminhos e verifique GPU.
- Recomenda-se testar com diferentes épocas (ex.: 30 e 60) para comparação, conforme enunciado.

## CNN Treinada do Zero

[CNN.ipynb](src/entrega_2/CNN.ipynb)

Neste notebook foi implementada uma Rede Neural Convolucional (CNN) treinada do zero para classificação de imagens, utilizando TensorFlow/Keras, na base criada em Google Drive.

Fluxo executado:
- Montagem do Google Drive (Colab):
  - from google.colab import drive; drive.mount('/content/drive')
- Definição de caminhos principais:
  - `base_dir = "/content/drive/MyDrive/Cap6_Fase1"`
  - `train_dir` e `test_dir` para pastas de treino e teste.
- Preparação do ambiente:
  - Importação de bibliotecas: TensorFlow, Keras, etc.
- Modelo usado:
  - CNN customizada com camadas Conv2D, MaxPooling, Flatten, Dense e Dropout.

Hiperparâmetros de treino (conforme notebook):
- epochs: 30 (com EarlyStopping, patience=5)
- batch_size: 16
- img_height, img_width: 128, 128
- Data augmentation: rotation_range=30, width_shift_range=0.1, etc.

Arquitetura da CNN:
- Conv2D(32, (3,3), relu) -> MaxPooling2D((2,2))
- Conv2D(64, (3,3), relu) -> MaxPooling2D((2,2))
- Conv2D(128, (3,3), relu) -> MaxPooling2D((2,2))
- Flatten -> Dense(128, relu) -> Dropout(0.5) -> Dense(num_classes, softmax)

Inferência / geração de resultados:
- Avaliação no conjunto de teste após treinamento.
- Visualizações: gráficos de acurácia/loss, histograma de predições.

## Avaliação (síntese retirada do próprio notebook)
- Facilidade de uso / integração: Simples e direto, com controle total sobre as camadas e ajustes, ideal para aprendizado.
- Precisão: Acurácia de validação máxima de 98,75% e final no teste de 87,50%. Boa generalização, mas com leve tendência a overfitting.
- Tempo de treinamento: Cada época levou 12-16 segundos, treinamento rápido.
- Tempo de inferência: Extremamente rápido, adequado para aplicações em tempo real.

## Como reproduzir (passo a passo mínimo no Colab)
1. Abrir o notebook `src/entrega_2/CNN.ipynb` no Colab.
2. Montar o Drive: `from google.colab import drive; drive.mount('/content/drive')`.
3. Verificar caminhos: `base_dir`, `train_dir`, `test_dir`.
4. Executar células de importação e definição de geradores de imagens.
5. Definir e compilar o modelo CNN.
6. Treinar com `model.fit()`, usando EarlyStopping.
7. Avaliar e visualizar métricas.

## Arquivos gerados e local de salvamento
- Modelo treinado: Salvo implicitamente no Colab, pode ser exportado com `model.save()`.
- Gráficos e visualizações: Gerados no notebook.

## Observações e recomendações
- Adequado para datasets pequenos, mas pode sofrer overfitting sem augmentation suficiente.
- Comparar com YOLO para ver diferenças em detecção vs. classificação.

# Ir Além 1 

## Resumo da implementação

### [https://youtu.be/StURW4G3Hww](https://youtu.be/StURW4G3Hww)

[yolo_padrao_fiap.ipynb](src/ir_alem_1/yolo_padrao_fiap_esp32cam.ipynb)

Neste notebook foi desenvolvido um Sistema de Reconhecimento com ESP32-CAM e YOLO, foi utilizado o modelo da Entrega 1 para integrar com o ESP32-WROVER-DEV (CAM).

Fluxo executado:
- Montagem do Google Drive (Colab):
  - from google.colab import drive; drive.mount('/content/drive')
- Definição de caminhos principais:
  - `DATASET_PATH = "/content/drive/MyDrive/FASE6_CAP1/yolo/data.yaml"` (arquivo YAML com paths do dataset e classes)
  - `teste_path = "/content/drive/MyDrive/FASE6_CAP1/yolo/test"` (pasta com imagens de teste)
- Preparação do ambiente:
  - Clone do repositório YOLO (quando necessário) e instalação de dependências.
- Modelo usado:
  - `ultralytics` YOLOv8 (pesos iniciais: `yolov8s.pt`).
- Codigo do ESP32 para conexão via WIFI
- Chamada da função Screem por IP para executar o código em tempo real

## Objetivo
Implementar um sistema de visão computacional em tempo real utilizando um módulo **ESP32-CAM físico**, capaz de reconhecer **bananas e maçãs** com o modelo YOLO treinado na Entrega 1.

## Funcionamento
O ESP32-CAM transmite imagens via Wi-Fi para o Python, que processa o stream usando o modelo `best.pt` e realiza a detecção dos objetos em tempo real.

## Tecnologias Utilizadas
- YOLOv5 (Ultralytics)
- Python + OpenCV
- ESP32-CAM (Arduino IDE)
- Google Colab / Jupyter

## Demonstração
[Assista ao vídeo no YouTube (não listado)](link_do_video_aqui)


# Ir Além 2

## Criar Dataset Segmentado

### [https://youtu.be/dfWgIeiQotM](https://youtu.be/dfWgIeiQotM)

[criar_dataset_segmentado.ipynb](src/ir_alem_2/criar_dataset_segmentado.ipynb)

Neste notebook é baixado um dataset de imagens de animes e realizada a segmentação das imagens para criar crops focados nos objetos principais, preparando o dataset para treinamento de CNNs.

Fluxo executado:
- Download do dataset via KaggleHub.
- Seleção de classes específicas (ex.: Dragon Ball Z, Samurai X).
- Aplicação de segmentação para extrair regiões de interesse (crops).
- Salvamento do dataset segmentado em pasta local.

Arquitetura/Abordagem:
- Utiliza técnicas de segmentação para focar em objetos centrais das imagens.

Avaliação:
- Facilidade: Automatizado, mas requer ajustes manuais para segmentação precisa.
- Resultado: Dataset preparado com imagens cropped, melhorando a performance de modelos subsequentes.

## CNN Inicial sem Crop

[cnn_inicial_sem_crop.ipynb](src/ir_alem_2/cnn_inicial_sem_crop.ipynb)

Neste notebook é treinada uma CNN do zero sem segmentação prévia, utilizando um dataset baixado do Kaggle.

Fluxo executado:
- Download e preparação do dataset (ex.: anime images).
- Definição de geradores de imagens com redimensionamento.
- Construção e treinamento de uma CNN simples (Conv2D, MaxPooling, Dense).
- Avaliação com matriz de confusão.

Arquitetura:
- Conv2D(32, 3, relu) -> MaxPooling2D -> Conv2D(64, 3, relu) -> MaxPooling2D -> Flatten -> Dense(128, relu) -> Dropout(0.3) -> Dense(num_classes, softmax)

Hiperparâmetros:
- epochs: 50 (com EarlyStopping, patience=5)
- batch_size: 32
- img_size: (200, 200)

Avaliação:
- Precisão: Acurácia final inferior comparada a versões com crop, devido à complexidade das imagens não segmentadas.
- Tempo: Treinamento rápido, mas menor performance.

## CNN Inicial com Crop

[cnn_inicial_com_crop.ipynb](src/ir_alem_2/cnn_inicial_com_crop.ipynb)

Neste notebook é treinada uma CNN do zero utilizando o dataset segmentado (com crops) criado anteriormente.

Fluxo executado:
- Carregamento do dataset segmentado.
- Construção e treinamento de CNN similar à versão sem crop.
- Avaliação com matriz de confusão.

Arquitetura: Idêntica à CNN sem crop.

Hiperparâmetros: Idênticos.

Avaliação:
- Precisão: Acurácia impressionante de 0.96, demonstrando o benefício da segmentação prévia.
- Tempo: Treinamento eficiente, com EarlyStopping.

## Transfer Learning

[transfer_learning.ipynb](src/ir_alem_2/transfer_learning.ipynb)

Neste notebook é aplicado Transfer Learning utilizando ResNet50 pré-treinada no ImageNet, com o dataset segmentado.

Fluxo executado:
- Carregamento do ResNet50 (pesos ImageNet, sem top layers).
- Congelamento das camadas base.
- Adição de camadas densas para classificação.
- Treinamento apenas das camadas superiores.

Arquitetura:
- ResNet50 (base congelada) -> GlobalAveragePooling2D -> Dense(128, relu) -> Dropout(0.3) -> Dense(num_classes, softmax)

Hiperparâmetros:
- epochs: 50 (EarlyStopping)
- batch_size: 32

Avaliação:
- Precisão: Acurácia de 0.96, superior a CNNs treinadas do zero devido ao aproveitamento de features pré-treinadas.
- Tempo: Treinamento mais rápido e eficiente.

## Fine Tuning

[fine_tuning.ipynb](src/ir_alem_2/fine_tuning.ipynb)

Neste notebook é realizado Transfer Learning seguido de Fine Tuning, ajustando algumas camadas da ResNet50 para o dataset específico.

Fluxo executado:
- Transfer Learning inicial (como acima).
- Descongelamento de camadas superiores da ResNet50.
- Treinamento com learning rate menor para fine tuning.

Arquitetura: Similar ao Transfer Learning, mas com ajuste fino das camadas base.

Avaliação:
- Precisão: Melhor performance potencial comparada ao Transfer Learning puro, adaptando melhor ao dataset.
- Tempo: Mais demorado devido ao ajuste de mais parâmetros.

## 📁 Estrutura do repositório

- README.md               -> documentação principal do projeto
- assets/                 -> logos e imagens de suporte
  - logo-fiap.png
- src/                    -> notebooks e scripts
  - entrega_1/            -> notebooks para Entrega 1
    - yolo_padrao_fiap.ipynb
  - entrega_2/            -> notebooks para Entrega 2
    - CNN.ipynb
    - yolo7.ipynb
  - ir_alem_2/            -> notebooks para Ir Além 2
    - cnn_inicial_com_crop.ipynb
    - cnn_inicial_sem_crop.ipynb
    - criar_dataset_segmentado.ipynb
    - fine_tuning.ipynb
    - transfer_learning.ipynb

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
