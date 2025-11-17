from database.models.sensor import TipoSensorEnum, TipoSensor, Sensor, LeituraSensor
from database.tipos_base.db import Database
from datetime import datetime
from fastapi import APIRouter

from src.ir_alem_2.src.api.base.leitura_request import LeituraRequest

receber_router = APIRouter()

@receber_router.post("")
@receber_router.post("/")
def receber_leitura(request: LeituraRequest):

    print(f"Recebendo leitura para o sensor com serial: {request.serial}", request)

    now = datetime.now()

    with Database.get_session() as session:
        sensores = session.query(Sensor).filter(Sensor.cod_serial == request.serial).filter().all()

        if not sensores:
            return {
                "status": "error",
                "message": f"Sensor com serial '{request.serial}' não encontrado."
            }

        for sensor in sensores:

            tipo = session.query(TipoSensor).filter(TipoSensor.id == sensor.tipo_sensor_id).first()

            if not tipo:
                return {
                    "status": "error",
                    "message": f"Tipo de sensor para o sensor com serial '{request.serial}' não encontrado."
                }

            if tipo.tipo == TipoSensorEnum.TEMPERATURA and request.temperature is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor= request.temperature
                )
            elif tipo.tipo == TipoSensorEnum.UMIDADE and request.humidity is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.humidity
                )
            elif tipo.tipo == TipoSensorEnum.LUX and request.lux is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.lux
                )
            elif tipo.tipo == TipoSensorEnum.UMIDADE_SOLO and request.soil_humidity is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.soil_humidity
                )
            else:
                continue
            session.add(nova_leitura)
            print('Nova leitura salva:', nova_leitura)

        session.commit()


    return {
        "status": "success",
        "message": "Leitura recebida com sucesso",
    }
