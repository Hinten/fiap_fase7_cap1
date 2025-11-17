from src.ir_alem_2.src.dashboard.main import main as dashboard_main
from dotenv import load_dotenv


import os

def main():
    """
    Função principal do aplicativo Streamlit.
    para rodar o aplicativo, execute o seguinte comando:
    streamlit run dashboard_ir_alem_2.py
    """
    load_dotenv()

    dashboard_main()

if __name__ == "__main__":
    main()
