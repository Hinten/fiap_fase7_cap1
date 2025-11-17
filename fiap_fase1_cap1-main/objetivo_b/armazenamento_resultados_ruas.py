import json

def salvar_resultado_ruas(ruas_min: int, ruas_max: int, arquivo="resultados_ruas.json"):
    """Função para salvar os resultados de ruas em um arquivo JSON."""
    dados = {
        'ruas_min': ruas_min,
        'ruas_max': ruas_max
    }
    with open(arquivo, 'w') as f:
        f.write(json.dumps(dados))
    print("Resultados das ruas salvos com sucesso.")

def carregar_resultado_ruas(arquivo="resultados_ruas.json"):
    """Função para carregar os resultados de ruas do arquivo JSON."""
    try:
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            return dados['ruas_min'], dados['ruas_max']
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum dado carregado.")
        return None, None