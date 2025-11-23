import streamlit as st
from database.models.sensor import LeituraSensor, Sensor, TipoSensorEnum, TipoSensor
import matplotlib.pyplot as plt


def _principal():
    st.title("Gráfico de Leitura dos Sensores")

    leituras = LeituraSensor.as_dataframe_all()

    if leituras.empty:
        st.warning("Nenhuma leitura de sensor disponível.")
        return

    # Buscar os tipos de sensores para cada leitura
    # Supondo que leituras tenha sensor_id
    sensores = Sensor.as_dataframe_all()[['id', 'tipo_sensor_id']]
    tipos = TipoSensor.as_dataframe_all()[['id', 'tipo']]
    tipos['tipo_nome'] = tipos['tipo'].apply(lambda x: TipoSensorEnum(x).__str__())

    # Merge para trazer o tipo_nome para cada leitura
    leituras = leituras.merge(sensores, left_on='sensor_id', right_on='id', suffixes=('', '_sensor'))
    leituras = leituras.merge(tipos, left_on='tipo_sensor_id', right_on='id', suffixes=('', '_tipo'))

    # Pivotando o dataframe
    df_pivot = leituras.pivot_table(index='data_leitura', columns='tipo_nome', values='valor', aggfunc='mean')

    # Plotando o gráfico
    fig, ax = plt.subplots(figsize=(10, 5))
    df_pivot.plot(ax=ax)
    ax.set_xlabel('Data de Leitura')
    ax.set_ylabel('Valor')
    ax.set_title('Leituras dos Sensores por Tipo ao Longo do Tempo')
    st.pyplot(fig)

    st.dataframe(df_pivot)

    st.write("Este gráfico mostra a média das leituras dos sensores ao longo do tempo, categorizadas por tipo de sensor.")


def get_principal_page() -> st.Page:
    """
    Função para retornar a página principal.
    :return: st.Page - A página principal do aplicativo.
    """
    return st.Page(
        _principal,
        title="Principal",
        url_path="/"
    )