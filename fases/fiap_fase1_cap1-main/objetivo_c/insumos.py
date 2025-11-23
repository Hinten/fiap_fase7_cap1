from objetivo_a.culturas import CULTURA_1, CULTURA_2

culturas = []

def calcular_area(tipo: str, base: float, altura: float):
    return base * altura

#Fontes: https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/milho/producao/manejo-do-solo-e-adubacao/adubacao-e-fertilidade-do-solo/adubacao-mineral
# https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/cana/producao/correcao-e-adubacao/diagnose-das-necessidades-nutricionais/recomendacao-de-correcao-e-adubacao/adubacao-mineral

class Insumos:
    tipo: str
    fosforo: float
    potassio: float

    def __init__(self, tipo: str, fosforo: float, potassio: float):
        self.tipo = tipo
        self.fosforo = fosforo
        self.potassio = potassio

def calcular_insumos(tipo, area: float) -> Insumos:
    area_hectares = area / 10000

    if tipo == CULTURA_1:
        fosforo = 120 * area_hectares
        potassio = 200 * area_hectares

        return Insumos(tipo, fosforo, potassio)

    elif tipo == CULTURA_2:
        fosforo = 100 * area_hectares
        potassio = 120 * area_hectares

        return Insumos(tipo, fosforo, potassio)

    raise  Exception(f"Tipo de cultura não encontrado {tipo}")


class Espacamento:
    area: float
    min:float
    max: float

    def __init__(self, area: float, min: float, max: float):
        self.area = area
        self.min = min
        self.max = max

    def calcula_ruas_min_max(self) -> tuple:
        ruas_min = int(self.area // self.max)
        ruas_max = int(self.area // self.min)

        return ruas_min, ruas_max


def calcula_espacamento(cultura_nome: str, area:float) -> Espacamento:
    if cultura_nome == CULTURA_1:
        espacamento_min = 1.0
        espacamento_max = 1.8
        return Espacamento(area, espacamento_min, espacamento_max)

    if cultura_nome == CULTURA_2:
        espacamento_min = 0.5
        espacamento_max = 0.9
        return Espacamento(area, espacamento_min, espacamento_max)

    raise Exception(f"Cultura não encontrada {cultura_nome}")

def adicionar_cultura():
    print("\nCadastro de nova cultura:")
    tipo = input("Digite o tipo de cultura (Cana-de-açúcar ou Milho): ")

    if tipo not in ["Cana-de-açúcar", "Milho"]:
        print("Cultura inválida! Tente novamente.")
        return

    base = float(input("Digite a largura do terreno (em metros): "))
    altura = float(input("Digite o comprimento do terreno (em metros): "))
    area = calcular_area(tipo, base, altura)

    insumos_necessarios = calcular_insumos(tipo, area)

    culturas.append({
        "Tipo": tipo,
        "Area (m²)": area,
        "Fosforo (kg)": insumos_necessarios["Fosforo (kg)"],
        "Potassio (kg)": insumos_necessarios["Potassio (kg)"]
    })
    print("\nCultura adicionada com sucesso!\n")

def exibir_culturas():
    if not culturas:
        print("\nNenhuma cultura cadastrada ainda!\n")
        return

    print("\nCulturas cadastradas:")
    for i, cultura in enumerate(culturas):
        print(f"{i + 1}. Tipo: {cultura['Tipo']} - Area: {cultura['Area (m²)']} m² - Fosforo: {cultura['Fosforo (kg)']} kg - Potassio: {cultura['Potassio (kg)']} kg")

def menu():
    while True:
        print("\nSistema de Gerenciamento Agrícola")
        print("1 - Adicionar Cultura")
        print("2 - Exibir Culturas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cultura()
        elif opcao == "2":
            exibir_culturas()
        elif opcao == "3":
            print("\nSaindo do sistema... Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()