# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Projeto: fiap_fase5_cap1

## Atividade em Grupo: FIAP - 1TIAOB - 2025/1 - Fase5 Cap 1

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

# 🌾 Entrega 1 – Análise e Predição de Rendimento Agrícola

#### 🎥 Vídeo Explicativo

- **Entrega 1 (Machine Learning):** [https://www.youtube.com/watch?v=XXQaWhhLs8k](https://www.youtube.com/watch?v=XXQaWhhLs8k) *(não listado)*  

## 📄 Descrição

Este projeto tem como objetivo analisar dados de rendimento agrícola de plantações, buscando compreender os fatores que influenciam a produtividade das safras. 
O foco está na identificação de padrões, tendências e outliers nos dados, permitindo destacar cenários atípicos que podem afetar a produção agrícola. 
O fluxo de trabalho integra análise exploratória, clusterização e modelagem preditiva, oferecendo uma abordagem completa de ciência de dados aplicada ao contexto agrícola. 
Inicialmente, realiza-se a análise exploratória para investigar as características do dataset, incluindo estatísticas descritivas, visualizações de distribuições e relações entre variáveis, além da identificação de inconsistências ou valores discrepantes. 
Em seguida, aplicam-se técnicas de clusterização, como HDBSCAN, para agrupar observações com comportamentos semelhantes e detectar cenários fora do padrão, permitindo reconhecer padrões emergentes e segmentar diferentes perfis de rendimento. 
Por fim, são construídos cinco modelos preditivos distintos utilizando regressão, com pré-processamento, treinamento, validação e avaliação automatizados pelo PyCaret. O desempenho dos modelos é comparado por métricas como R², RMSE e MAE, garantindo a seleção de abordagens robustas para previsão da produtividade. 
Dessa forma, o projeto fornece uma solução completa para prever rendimento agrícola e apoiar decisões estratégicas na gestão das plantações.

---

## 🗂 Estrutura do Projeto
- [crop_yield.csv](src/entrega_1/crop_yield.csv) – Base de dados com informações sobre rendimento das plantações.
- [treinamento_ia.ipynb](src/entrega_1/treinamento_ia.ipynb) – Notebook com código completo, visualizações e modelagem.
- [top_models](src/entrega_1/top_models) – Pasta contendo os cinco melhores modelos treinados.

---

## 🛠 Tecnologias e Bibliotecas
- **Python 3.11**
- Bibliotecas:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `hdbscan`
  - `pycaret`  

**ATENÇÃO**: Recomenda-se o uso de um ambiente virtual com Python na versão específica 3.11.x para a execução do Pycaret.
Mais informações sobre a sua instalação, verificar na documentação do [Pycaret](https://pycaret.gitbook.io/docs/get-started/installation).

---

## 🚀 Etapas do Projeto

### 1️⃣ Análise Exploratória de Dados (EDA)
- Inspeção do dataset (`head`, `shape`, `columns`, `sample`).
- Visualizações:
  - Pairplots para explorar relações entre variáveis.
  - Boxplots para identificar outliers.
- Objetivo: compreender padrões, tendências e inconsistências nos dados.

### 2️⃣ Clusterização e Identificação de Outliers
- Algoritmo: **HDBSCAN** aplicado a colunas numéricas.
- Visualização de clusters para identificar agrupamentos naturais e outliers.

### 3️⃣ Modelagem Preditiva
- Pré-processamento automatizado com **PyCaret**.
- Objetivo: prever a variável `Yield` (rendimento da safra).
- Divisão treino/teste: 80/20.
- Treinamento de cinco modelos de regressão distintos.

### 4️⃣ Seleção e Avaliação dos Melhores Modelos
- Métrica principal: **R² score**.
- Outras métricas: **RMSE** e **MAE**.
- Visualizações:
  - Gráficos de erro
  - Importância das variáveis

### 5️⃣ Conclusão
- O fluxo completo permitiu identificar padrões, outliers e construir modelos robustos de previsão de rendimento.
- HDBSCAN ajudou a detectar cenários discrepantes.
- PyCaret automatizou seleção, treinamento e avaliação de múltiplos algoritmos.

---

## ▶️ Como Executar
1. Instale o Python na versão 3.11.x.
2. Abra o notebook [treinamento_ia.ipynb](src/entrega_1/treinamento_ia.ipynb).
3. Execute as células na ordem apresentada para reproduzir a análise, clusterização e modelagem preditiva.

# Entrega 2 – Estimativa de Custos na AWS

#### 🎥 Vídeo Explicativo

- **Entrega 2 (AWS Cloud):** [https://www.youtube.com/watch?v=5PAdMoMSE8A](https://www.youtube.com/watch?v=5PAdMoMSE8A) *(não listado)*    

## 📜 Descrição

Este projeto tem como objetivo compreender o funcionamento da computação em nuvem e justificar a escolha de recursos adequados para hospedar uma aplicação simples utilizando a AWS (Amazon Web Services). Durante a atividade, exploramos diferentes serviços da AWS, estimamos custos e comparamos preços entre regiões distintas para fundamentar a tomada de decisão.

Com a API e os modelos de Machine Learning prontos, foi necessário estimar os custos de execução na nuvem AWS.  
Para isso, foi utilizada a **AWS Pricing Calculator** com a seguinte configuração:

- **2 vCPUs**
- **1 GiB de memória**
- **Até 5 Gigabit de rede**
- **50 GB de armazenamento HDD (EBS sc1)**
- **Linux**
- **On-Demand (100%)**

**Comparação de Custos por Região:**

| Região                   | Custo Mensal (On-Demand) | Upfront |
|--------------------------|--------------------------|---------|
| **US East (N. Virginia)** | **USD 6.88**             | 0       |
| **South America (São Paulo)** | **USD 11.22**            | 0       |

📊 **Conclusão**:  
- N. Virginia é ~40% mais barato.  
- São Paulo é mais caro, mas essencial em casos de **restrições legais** ou **necessidade de baixa latência** no Brasil.

---

#### 📑 Exportações Oficiais da Calculadora AWS

<p align="center">
  <img src="assets/estimativa_entrega_2.JPG" alt="Circuito Sensor" border="0" width=70% height=70%>
</p>


- [PDF Estimativa N. Virginia](src/entrega_2/aws-n-virginia.pdf)
- [PDF Estimativa São Paulo](src/entrega_2/aws-sao-paulo.pdf)

*(Esses PDFs foram gerados diretamente no **AWS Pricing Calculator**, garantindo a rastreabilidade dos valores apresentados.)*

---

# Ir Além 1 🌱 Sistema de Monitoramento de Estufa

O grupo desenvolveu o Ir Além 1 solicitado, podendo ser encontrado na pasta [src/ir_alem_1](src/ir_alem_1).

O Readme completo do Ir Além 1 pode ser encontrado em [src/ir_alem_1/README.md](src/ir_alem_1/README.md).

#### 🎥 Vídeo Explicativo

- **Ir Além 1 🌱 Sistema de Monitoramento de Estufa:** [https://www.youtube.com/watch?v=QsNpCC74HIo](https://www.youtube.com/watch?v=QsNpCC74HIo) *(não listado)*


# Ir Além 2 🌱 Projeto de monitoramento inteligente de plantas

O grupo desenvolveu o Ir Além 2 solicitado, podendo ser encontrado na pasta [src/ir_alem_2](src/ir_alem_2).

O Readme completo do Ir Além 2 pode ser encontrado em [src/ir_alem_2/README.md](src/ir_alem_2/README.md).

#### 🎥 Vídeo Explicativo

- ** Ir Além 2 🌱 Projeto de monitoramento inteligente de plantas:** [https://www.youtube.com/watch?v=kxKfG09zvTg](https://www.youtube.com/watch?v=kxKfG09zvTg) *(não listado)*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.streamlit</b>: Pasta que contém arquivos de configuração do Streamlit, como o tema da interface e a organização da barra lateral.
- <b>assets</b>: Diretório destinado ao armazenamento de elementos não estruturados do projeto, como imagens e ícones utilizados no dashboard.
- <b>packages</b>: Pasta que contém pacotes compartilhados utilizados no projeto.
- <b>src</b>: Diretório principal que contém todo o código-fonte desenvolvido ao longo das fases do projeto. Ele está organizado nos seguintes submódulos:
  - <b>entrega_1</b>: Contém o código e os notebooks relacionados à Análise e Predição de Rendimento Agrícola, incluindo a análise exploratória, clusterização e modelagem preditiva. ([entrega_1](src/entrega_1/))
  - <b>entrega_2</b>: Contém os documentos e arquivos relacionados à Estimativa de Custos na AWS, incluindo as exportações oficiais da calculadora de preços da AWS. ([entrega_2](src/entrega_2/))
  - <b>ir_alem_1</b>: Contém o código e os arquivos do projeto "Ir Além 1", que é um sistema de monitoramento de estufa utilizando ESP32, sensores ambientais. ([ir_alem_1](src/ir_alem_1/))
  - <b>ir_alem_2</b>: Contém o código e os arquivos do projeto "Ir Além 2", que é um sistema de monitoramento inteligente de plantas utilizando ESP32, sensores ambientais, API em Python (FastAPI), dashboard interativo (Streamlit) e modelo de Machine Learning para previsão da saúde vegetal. ([ir_alem_2](src/ir_alem_2/))
- <b>.env</b>: Arquivo de configuração que contém as chaves de API e outras variáveis de ambiente necessárias para o funcionamento do sistema. É necessário criar este arquivo na raiz do projeto, conforme orientações na seção "Arquivo de Configuração".
- <b>.gitignore</b>: Arquivo que especifica quais arquivos e pastas devem ser ignorados pelo Git, evitando que informações sensíveis ou desnecessárias sejam versionadas. É importante garantir que o arquivo `.env` esteja incluído neste arquivo para evitar o upload de chaves de API e outras informações sensíveis.
- <b>dashboard_ir_alem_2.py</b>: Arquivo principal do dashboard, responsável por iniciar a aplicação web interativa utilizando Streamlit.
- <b>diagram.json</b>: Arquivo JSON que contém o diagrama de conexão dos sensores utilizados no projeto, facilitando a compreensão da arquitetura do sistema.
- <b>platformio.ini</b>: Arquivo de configuração do PlatformIO, utilizado para definir as especificações do projeto embarcado com ESP32, incluindo as bibliotecas necessárias e as configurações de compilação.
- <b>README</b>: Arquivo de documentação do projeto (este que está sendo lido), com orientações gerais, instruções de uso e contextualização.
- <b>requirements.txt</b>: Arquivo que lista todas as dependências do projeto, necessário para a instalação do ambiente virtual. Deve ser utilizado com o comando `pip install -r requirements.txt` para instalar as bibliotecas necessárias.
- <b>wokwi.toml</b>: Arquivo de configuração para simulação do ESP32 na plataforma Wokwi, permitindo testar o código embarcado sem a necessidade de hardware físico.


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


