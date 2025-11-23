import logging
import os
import streamlit as st

from dashboard_streamlit.login import login_sqlite, login_view
from logger_basico.config import configurar_logger
from src.ir_alem_2.src.dashboard.api_sensor import iniciar_api_sensor
from src.ir_alem_2.src.dashboard.navigator import navigation
from src.ir_alem_2.src.dashboard.setup import setup


def main():
    """
    Função principal do aplicativo Streamlit.
    para rodar o aplicativo, execute o seguinte comando:
    streamlit run main_dash.py
    :return:
    """
    configurar_logger("dashboard.log")
    st.set_page_config(layout="wide") # deixa a página mais larga

    sql_lite:bool = os.environ.get("SQL_LITE", "false").lower() == "true"

    if not st.session_state.get('logged_in', False):
        logging.debug('acessando login')

        if sql_lite:
            login_sqlite()
        else:
            login_view()
    else:
        logging.debug('acessando dashboard')
        setup()
        iniciar_api_sensor()
        navigation()

if __name__ == "__main__":
    main()
