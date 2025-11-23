from fastapi import APIRouter
from src.ir_alem_2.src.api.base.leitura_request import LeituraRequest
from src.ir_alem_2.src.machine_learning.previsao import fazer_previsao

saude_router = APIRouter()

@saude_router.post("")
@saude_router.post("/")
def prever_saude(request: LeituraRequest):

    previsao = fazer_previsao(
        Soil_Moisture=request.soil_humidity,
        Ambient_Temperature=request.temperature,
        Humidity=request.humidity,
        Light_Intensity=request.lux,
    )

    print(f"Previsão de saúde da planta: {'Saudável' if previsao == True else 'Não Saudável'}")

    return {
        "saude": bool(previsao)
    }
