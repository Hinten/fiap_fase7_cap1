from objetivo_c.insumos import calcula_espacamento, calcular_insumos
from objetivo_d.vetor_de_dados import Area

def apresentacao_de_dados(tipo: str, area:float):

    resposta = ''

    espacamento = calcula_espacamento(tipo, area)
    insumos = calcular_insumos(tipo, area)

    ruas = espacamento.calcula_ruas_min_max()
    resposta += f"Número de ruas de plantio: {ruas[0]} a {ruas[1]} ruas\n"
    resposta += f"Quantidade de Fósforo: {insumos.fosforo:.2f} kg\n"
    resposta += f"Quantidade de Potássio: {insumos.potassio:.2f} kg\n"
    return  resposta





