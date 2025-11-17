# Fase 1: Base de Dados Inicial

## 📋 Descrição

Esta fase implementa a base de dados inicial do sistema com cálculos de área de plantio, gestão de insumos e integração com API meteorológica.

## 🎯 Objetivos

- Cálculo de área de plantio
- Gestão de insumos agrícolas
- Integração com API meteorológica pública
- Análise estatística de dados meteorológicos em R

## 📂 Estrutura

```
phase1/
├── calculos/              # Cálculos de área e insumos
├── api_meteorologica/     # Integração com serviço meteorológico
└── analise_estatistica/   # Scripts R para análise
```

## 🔧 Como Usar

### Executar via Dashboard
1. Acesse a dashboard principal
2. Vá para "Fase 1: Meteorologia"
3. Clique nos botões correspondentes

### Executar Diretamente

```bash
# Buscar dados meteorológicos
cd phase1/api_meteorologica
python fetch_weather.py

# Executar análise estatística em R
cd ../analise_estatistica
Rscript analise.R
```

## 📦 Dependências Específicas

```
requests
pandas
numpy
matplotlib
```

**R packages:**
- tidyverse
- ggplot2
- forecast
- lubridate

## 🔗 Repositório Original

[fiap_fase1_cap1](https://github.com/Hinten/fiap_fase1_cap1)

## 📝 O Que Trazer do Repositório Original

- Scripts de cálculos de área
- Integração com API meteorológica
- Scripts R de análise estatística
- Dados de exemplo (CSV)
