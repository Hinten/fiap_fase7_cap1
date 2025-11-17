"""
Dashboard Principal Unificada - FIAP Fase 7
Sistema de Gestão para Agronegócio

Este é o ponto de entrada principal da aplicação Streamlit que integra
todas as funcionalidades das Fases 1-6.
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title=os.getenv("DASHBOARD_TITLE", "Sistema de Gestão Agronegócio - FIAP Fase 7"),
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Hinten/fiap_fase7_cap1',
        'Report a bug': 'https://github.com/Hinten/fiap_fase7_cap1/issues',
        'About': '''
        # Sistema de Gestão para Agronegócio
        ## FIAP - Fase 7
        
        Integração completa das Fases 1 a 6:
        - Fase 1: Meteorologia e análise de dados
        - Fase 2: Banco de dados estruturado
        - Fase 3: IoT e automação inteligente
        - Fase 4: Machine Learning e análises preditivas
        - Fase 5: Cloud Computing (AWS) e segurança
        - Fase 6: Visão computacional com YOLO
        
        **Desenvolvido para o programa FIAP**
        '''
    }
)

# Estilo customizado
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌱 Sistema de Gestão")
st.sidebar.markdown("**FIAP - Fase 7**")
st.sidebar.markdown("---")

# Menu de navegação
page = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Home",
        "☁️ Fase 1: Meteorologia",
        "🗄️ Fase 2: Banco de Dados",
        "🤖 Fase 3: IoT e Sensores",
        "📊 Fase 4: Machine Learning",
        "👁️ Fase 6: Visão Computacional",
        "📧 Sistema de Alertas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Ações Rápidas")

# Botões de ação rápida
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("▶️ Sensores"):
        st.sidebar.info("Iniciando sensores...")

with col2:
    if st.button("📸 YOLO"):
        st.sidebar.info("Processando imagens...")

if st.sidebar.button("🚨 Alerta Teste"):
    st.sidebar.success("Alerta enviado!")

# Status do sistema
st.sidebar.markdown("---")
st.sidebar.subheader("Status do Sistema")
st.sidebar.success("✅ Banco de Dados")
st.sidebar.info("⏸️ Sensores IoT")
st.sidebar.warning("⚠️ API Meteorológica")

# Conteúdo principal
if page == "🏠 Home":
    st.title("🌱 Sistema de Gestão para Agronegócio")
    st.markdown("### FIAP - Fase 7: Consolidação do Sistema")
    
    st.markdown("""
    Bem-vindo ao sistema integrado de gestão para agronegócio que consolida 
    todas as funcionalidades desenvolvidas nas Fases 1 a 6.
    """)
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Temperatura Média",
            value="28°C",
            delta="2°C"
        )
    
    with col2:
        st.metric(
            label="Umidade do Solo",
            value="65%",
            delta="-5%"
        )
    
    with col3:
        st.metric(
            label="Sensores Ativos",
            value="5",
            delta="0"
        )
    
    with col4:
        st.metric(
            label="Alertas Hoje",
            value="3",
            delta="1"
        )
    
    st.markdown("---")
    
    # Visão geral das fases
    st.subheader("📋 Funcionalidades por Fase")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Fase 1", "Fase 2", "Fase 3", "Fase 4", "Fase 5", "Fase 6"
    ])
    
    with tab1:
        st.markdown("### ☁️ Fase 1: Base de Dados e Meteorologia")
        st.markdown("""
        - ✅ Cálculo de área de plantio
        - ✅ Gestão de insumos
        - ✅ Integração com API meteorológica
        - ✅ Análise estatística em R
        """)
    
    with tab2:
        st.markdown("### 🗄️ Fase 2: Banco de Dados Estruturado")
        st.markdown("""
        - ✅ Modelo Entidade-Relacionamento (MER)
        - ✅ Diagrama Entidade-Relacionamento (DER)
        - ✅ Scripts SQL e migrações
        - ✅ Modelos ORM (SQLAlchemy)
        """)
    
    with tab3:
        st.markdown("### 🤖 Fase 3: IoT e Automação")
        st.markdown("""
        - ✅ Sensores DHT22 (temperatura/umidade)
        - ✅ Sensor LDR (luminosidade)
        - ✅ Automação de irrigação
        - ✅ API REST CRUD
        """)
    
    with tab4:
        st.markdown("### 📊 Fase 4: Dashboard e Machine Learning")
        st.markdown("""
        - ✅ Dashboard interativa Streamlit
        - ✅ Modelos de regressão e classificação
        - ✅ Previsões de irrigação
        - ✅ Visualizações interativas
        """)
    
    with tab5:
        st.markdown("### ☁️ Fase 5: Cloud Computing e Segurança")
        st.markdown("""
        - ✅ Infraestrutura AWS (EC2, RDS, S3)
        - ✅ Padrões ISO 27001/27002
        - ✅ Monitoramento CloudWatch
        - ✅ Backups automáticos
        """)
    
    with tab6:
        st.markdown("### 👁️ Fase 6: Visão Computacional")
        st.markdown("""
        - ✅ Modelo YOLO treinado
        - ✅ Detecção de pragas e doenças
        - ✅ Processamento de imagens
        - ✅ Integração com alertas
        """)
    
    st.markdown("---")
    
    # Alertas recentes
    st.subheader("🚨 Alertas Recentes")
    
    st.warning("⚠️ **Umidade baixa** - Setor A: 25% (limite: 30%)")
    st.info("ℹ️ **Manutenção programada** - Sensor DHT22-003 às 14:00")
    st.success("✅ **Sistema atualizado** - Novos dados meteorológicos disponíveis")

elif page == "☁️ Fase 1: Meteorologia":
    st.title("☁️ Fase 1: Meteorologia e Análise de Dados")
    st.info("📝 **Nota:** Esta página será implementada com os dados do repositório original da Fase 1.")
    st.markdown("""
    ### Funcionalidades
    - Buscar dados meteorológicos em tempo real
    - Visualizar histórico de temperatura e umidade
    - Análise estatística com R
    - Previsões meteorológicas
    """)
    
    if st.button("🔄 Atualizar Dados Meteorológicos"):
        st.success("Dados atualizados! (Implementar integração com API)")

elif page == "🗄️ Fase 2: Banco de Dados":
    st.title("🗄️ Fase 2: Banco de Dados")
    st.info("📝 **Nota:** Esta página será implementada com a integração do banco de dados.")

elif page == "🤖 Fase 3: IoT e Sensores":
    st.title("🤖 Fase 3: IoT e Sensores")
    st.info("📝 **Nota:** Esta página será implementada com a integração dos sensores IoT.")

elif page == "📊 Fase 4: Machine Learning":
    st.title("📊 Fase 4: Machine Learning")
    st.info("📝 **Nota:** Esta página será implementada com os modelos de ML da Fase 4.")

elif page == "👁️ Fase 6: Visão Computacional":
    st.title("👁️ Fase 6: Visão Computacional com YOLO")
    st.info("📝 **Nota:** Esta página será implementada com a detecção YOLO.")
    
    uploaded_file = st.file_uploader("Escolha uma imagem", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagem carregada", use_column_width=True)
        if st.button("🔍 Detectar Pragas/Doenças"):
            st.success("Processamento iniciado! (Implementar integração com YOLO)")

elif page == "📧 Sistema de Alertas":
    st.title("📧 Sistema de Alertas AWS")
    st.info("📝 **Nota:** Esta página será implementada com a integração SNS/SES.")
    
    with st.form("enviar_alerta"):
        st.subheader("Enviar Alerta Manual")
        
        tipo = st.selectbox("Tipo de Alerta", [
            "Umidade Baixa",
            "Temperatura Alta",
            "Praga Detectada",
            "Falha de Sensor",
            "Outro"
        ])
        
        mensagem = st.text_area("Mensagem")
        severidade = st.select_slider("Severidade", ["INFO", "WARNING", "CRITICAL"])
        setor = st.text_input("Setor")
        
        submitted = st.form_submit_button("🚨 Enviar Alerta")
        
        if submitted:
            st.success("✅ Alerta enviado com sucesso! (Implementar integração AWS)")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: #666;">
        <p>FIAP - Fase 7</p>
        <p>Sistema de Gestão para Agronegócio</p>
        <p>© 2024</p>
    </div>
""", unsafe_allow_html=True)
