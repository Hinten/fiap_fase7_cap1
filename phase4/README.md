# Fase 4: Dashboard Interativo com Data Science

## 📋 Descrição

Dashboard interativa com Machine Learning para análise preditiva e tomada de decisão.

## 🎯 Objetivos

- Dashboard Streamlit interativa
- Modelos de Machine Learning (Scikit-learn)
- Previsão de necessidades de irrigação
- Análise de tendências e padrões
- Visualizações interativas
- Recomendações automatizadas

## 📂 Estrutura

```
phase4/
├── streamlit_app/    # Aplicação Streamlit original
├── modelos_ml/       # Modelos treinados (.pkl)
└── notebooks/        # Jupyter Notebooks de análise
```

## 🤖 Modelos de Machine Learning

### Modelo de Regressão
- **Objetivo**: Previsão de consumo de água
- **Algoritmo**: Linear Regression / Random Forest
- **Features**: Temperatura, umidade, área, tipo de cultura
- **Target**: Litros de água necessários

### Modelo de Classificação
- **Objetivo**: Classificar necessidade de irrigação
- **Algoritmo**: Random Forest Classifier
- **Classes**: 
  - 0: Não irrigar
  - 1: Irrigação moderada
  - 2: Irrigação urgente

### Clustering
- **Objetivo**: Agrupar áreas similares
- **Algoritmo**: K-Means
- **Features**: Padrões de irrigação, solo, clima

## 🔧 Como Usar

### Executar Dashboard Original

```bash
cd phase4/streamlit_app
streamlit run app.py
```

### Treinar Modelos

```bash
cd phase4/notebooks
jupyter notebook treinamento.ipynb
```

### Fazer Previsões

```python
import joblib
import pandas as pd

# Carregar modelo
modelo = joblib.load('../modelos_ml/modelo_regressao.pkl')

# Fazer previsão
dados = pd.DataFrame({
    'temperatura': [28.5],
    'umidade': [45.0],
    'area_hectares': [10.0]
})

previsao = modelo.predict(dados)
print(f"Água necessária: {previsao[0]:.2f} litros")
```

## 📊 Visualizações Disponíveis

- Gráficos de linha temporal (séries temporais)
- Mapas de calor de umidade/temperatura
- Histogramas de distribuição
- Gráficos de dispersão (scatter)
- Box plots de variabilidade
- Dashboards interativos com Plotly

## 📦 Dependências Específicas

```
streamlit
scikit-learn
pandas
numpy
plotly
matplotlib
seaborn
joblib
```

## 🔗 Repositório Original

[fiap_fase4_cap1](https://github.com/Al1ce4-AI/fiap_fase4_cap1)

## 📝 O Que Trazer do Repositório Original

- Aplicação Streamlit completa
- Modelos ML treinados (.pkl)
- Notebooks de treinamento
- Scripts de pré-processamento
- Código de visualizações
- Integração com ESP32 (LCD, Serial Plotter)
