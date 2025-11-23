from fastapi import FastAPI
import uvicorn
import threading

from src.ir_alem_2.src.api.init_sensor import init_router
from src.ir_alem_2.src.api.prever_saude_planta import saude_router
from src.ir_alem_2.src.api.receber_leitura import receber_router

app = FastAPI()
app.include_router(init_router, prefix='/init')
app.include_router(receber_router, prefix='/leitura')
app.include_router(saude_router, prefix='/saude')

def _print_routes(app):
    for route in app.routes:
        if hasattr(route, "methods"):
            print(f"{list(route.methods)} {route.path}")

def iniciar_api():
    """
    Inicia a API
    """
    _print_routes(app)
    uvicorn.run(app, host="0.0.0.0", port=9080)


def inciar_api_thread_paralelo():
    """
    Inicia a API em uma thread separada.
    Isso permite que a API seja executada em segundo plano enquanto outras tarefas podem ser executadas
    """
    api_thread = threading.Thread(target=iniciar_api, daemon=True)
    api_thread.start()

if __name__ == "__main__":

    from database.tipos_base.db import Database
    Database.init_sqlite('../../../database.db')
    Database.create_all_tables(drop_if_exists=False)

    uvicorn.run(app, host="0.0.0.0", port=9080)