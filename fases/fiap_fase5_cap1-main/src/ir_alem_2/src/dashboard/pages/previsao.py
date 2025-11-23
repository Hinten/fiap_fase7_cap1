import streamlit as st
from src.ir_alem_2.src.machine_learning.previsao import fazer_previsao


def previsao_manual():

    st.title("Prever saúde da planta")

    st.header("Insire os dados abaixo para prever a saúde da planta")

    umidade_solo = st.number_input("Umidade do solo", value=30.0, step=1.0)
    umidade = st.number_input("Umidade do Ambiente", value=80.0, step=1.0)
    lux = st.number_input("Lux", value=15.0, step=1.0)
    temperatura = st.number_input("Temperatura", value=14.0, step=1.0)

    previsao = fazer_previsao(
        Soil_Moisture=umidade_solo,
        Ambient_Temperature=temperatura,
        Humidity=umidade,
        Light_Intensity=lux,
    )

    if st.button("Prever saúde da planta"):
        st.subheader("Resultado da Previsão")
        if previsao:
            st.success("A planta está saudável! 🌱")
        else:
            st.error("A planta não está saudável! ❌")



previsao_manual_page = st.Page(previsao_manual, title="Prever saúde da planta", icon="🤖")
