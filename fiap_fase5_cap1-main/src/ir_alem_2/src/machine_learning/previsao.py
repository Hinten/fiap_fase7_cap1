import joblib
import os
import pandas as pd

def fazer_previsao(
    Soil_Moisture:float,
    Ambient_Temperature:float,
    Humidity:float,
    Light_Intensity:float,
) -> bool:
    """
    Realiza a previsão usando o modelo salvo.
    :param Soil_Moisture: Umidade do solo.
    :param Ambient_Temperature: Temperatura ambiente.
    :param Humidity: Umidade.
    :param Light_Intensity: Intensidade da luz.
    :return: Previsão (True/False). (Saudável/Não Saudável)
    """

    pipeline_path = os.path.join(
        os.path.dirname(__file__),
        "Modelo",
        "melhor_modelo.pkl"
    )


    if not os.path.exists(pipeline_path):
        raise FileNotFoundError(f"Modelo não encontrado no caminho: {pipeline_path}")

    pipeline = joblib.load(pipeline_path)

    entrada = pd.DataFrame([[Soil_Moisture, Ambient_Temperature, Humidity, Light_Intensity]], columns=pipeline.column_names)

    previsao = pipeline.predict(entrada)

    return previsao[0]



if __name__ == "__main__":

    modelo_path = os.path.join(
        os.path.dirname(__file__),
        "Modelo",
        "melhor_modelo.pkl"
    )

    modelo = joblib.load(modelo_path)

    print(modelo.feature_names_in_) #aparece apenas quando tem um pipeline

    entrada = pd.DataFrame([[30.0, 25.0, 80.0, 300.0]], columns=modelo.column_names)

    print(modelo.predict(entrada))

