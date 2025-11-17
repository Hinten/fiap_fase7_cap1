# Dashboard Unificada - Fase 7

## 📋 Descrição

Dashboard principal que integra todas as funcionalidades das Fases 1-6 em uma interface única.

## 🎯 Funcionalidades

- Interface unificada para todos os serviços
- Botões para disparar serviços de cada fase
- Visualizações consolidadas
- Métricas em tempo real
- Sistema de navegação entre páginas
- Integração com banco de dados
- Controle do sistema de alertas

## 📂 Estrutura

```
dashboard/
├── app.py              # Aplicação principal Streamlit
├── pages/              # Páginas da dashboard
│   ├── home.py
│   ├── fase1_meteorologia.py
│   ├── fase2_banco_dados.py
│   ├── fase3_iot.py
│   ├── fase4_ml.py
│   ├── fase6_visao.py
│   └── alertas.py
├── components/         # Componentes reutilizáveis
│   ├── sidebar.py
│   ├── charts.py
│   ├── sensors.py
│   └── metrics.py
└── utils/              # Funções auxiliares
    ├── database.py
    ├── aws_client.py
    ├── sensor_simulator.py
    └── yolo_inference.py
```

## 🚀 Como Executar

```bash
cd dashboard
streamlit run app.py
```

Acesse: `http://localhost:8501`

## 📱 Páginas

### 🏠 Home
- Dashboard geral com métricas principais
- Status dos sensores
- Alertas recentes
- Resumo de todas as fases

### ☁️ Fase 1: Meteorologia
- Dados meteorológicos em tempo real
- Histórico de temperatura e umidade
- Previsões
- Botão para atualizar dados

### 🗄️ Fase 2: Banco de Dados
- Visualização de tabelas
- Consultas personalizadas
- Exportação de dados
- Estatísticas do banco

### 🤖 Fase 3: IoT e Sensores
- Monitoramento de sensores em tempo real
- Controle de irrigação
- Simulador de sensores
- Histórico de leituras

### 📊 Fase 4: Machine Learning
- Previsões de irrigação
- Análises preditivas
- Visualizações de tendências
- Retreinamento de modelos

### 👁️ Fase 6: Visão Computacional
- Upload de imagens
- Detecção de pragas/doenças
- Histórico de detecções
- Galeria de resultados

### 📧 Sistema de Alertas
- Configuração de alertas
- Histórico de notificações
- Teste de envio de e-mail/SMS
- Gerenciamento de destinatários

## 🔧 Componentes

### Sidebar
- Navegação entre páginas
- Botões de ação rápida
- Status do sistema
- Logout

### Charts
- Gráficos de linha temporal
- Gráficos de barras
- Mapas de calor
- Scatter plots

### Sensors
- Cards de sensores
- Indicadores visuais
- Alertas de status

### Metrics
- KPIs principais
- Comparações
- Tendências

## 💡 Exemplo de Uso

```python
import streamlit as st
import subprocess

st.title("🌱 Sistema de Gestão Agronegócio")

# Botão para executar serviço
if st.button("▶️ Iniciar Simulador IoT"):
    result = subprocess.run(
        ["python", "../phase3/sensores/simulador.py"],
        capture_output=True,
        text=True
    )
    st.success("Simulador iniciado!")
    st.code(result.stdout)
```

## 📊 Widgets Streamlit Utilizados

- `st.button()` - Botões de ação
- `st.sidebar` - Barra lateral
- `st.metric()` - Métricas
- `st.line_chart()` - Gráficos de linha
- `st.map()` - Mapas
- `st.dataframe()` - Tabelas
- `st.file_uploader()` - Upload de arquivos
- `st.form()` - Formulários
- `st.tabs()` - Abas
- `st.expander()` - Seções expansíveis

## 🎨 Customização

### Tema

Edite `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Layout

```python
# Layout wide
st.set_page_config(layout="wide")

# Colunas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperatura", "28°C")
```

## 🔒 Autenticação (Opcional)

Para adicionar login:

```python
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate(
    credentials,
    'fazenda_cookie',
    'fazenda_key',
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # Dashboard content
    pass
elif authentication_status == False:
    st.error('Username/password is incorrect')
```

## 📦 Dependências

```
streamlit
plotly
pandas
requests
subprocess
```

## 🐛 Debug

```bash
# Modo verbose
streamlit run app.py --logger.level=debug

# Limpar cache
streamlit cache clear
```
