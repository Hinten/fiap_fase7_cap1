from src.database.tipos_base.database import Database
from src.database.models.sensor import Sensor, TipoSensor, TipoSensorEnum, LeituraSensor
from datetime import datetime
from fastapi import APIRouter

from src.wokwi_api.base.leitura_request import LeituraRequest
from src.notificacoes.alertas import publicar_alerta_sensor

receber_router = APIRouter()

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

            if tipo.tipo == TipoSensorEnum.UMIDADE and request.umidade is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor= request.umidade
                )
            elif tipo.tipo == TipoSensorEnum.PH and request.ph is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.ph
                )
            elif tipo.tipo == TipoSensorEnum.POTASSIO and request.estado_potassio is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.estado_potassio
                )
            elif tipo.tipo == TipoSensorEnum.FOSFORO and request.estado_fosforo is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.estado_fosforo
                )
            elif tipo.tipo == TipoSensorEnum.RELE and request.estado_irrigacao is not None:
                nova_leitura = LeituraSensor(
                    sensor_id=sensor.id,
                    data_leitura=now,
                    valor=request.estado_irrigacao
                )
            else:
                continue
            session.add(nova_leitura)
            print('Nova leitura salva:', nova_leitura)

        session.commit()

    # Após salvar todas as leituras, avalia condições e envia alertas se necessário
    try:
        # Busca o sensor_id do primeiro sensor encontrado para usar no alerta
        # (todos os sensores têm o mesmo serial, então usamos o primeiro)
        if sensores:
            sensor_id = sensores[0].id
            
            # Converte estado_fosforo e estado_potassio para boolean
            # Valores do ESP32: 1 = OK/True, 0 = Crítico/False
            fosforo_ok = (request.estado_fosforo == 1) if request.estado_fosforo is not None else True
            potassio_ok = (request.estado_potassio == 1) if request.estado_potassio is not None else True
            irrigacao_ativa = (request.estado_irrigacao == 1) if request.estado_irrigacao is not None else False
            
            # Envia alerta se houver condições críticas
            publicar_alerta_sensor(
                sensor_id=sensor_id,
                umidade=request.umidade,
                ph=request.ph,
                fosforo_ok=fosforo_ok,
                potassio_ok=potassio_ok,
                irrigacao_ativa=irrigacao_ativa
            )
    except Exception as e:
        # Não falha a requisição se houver erro no envio de alerta
        print(f"[AVISO] Erro ao avaliar/enviar alerta: {str(e)}")

    return {
        "status": "success",
        "message": "Leitura recebida com sucesso",
    }
