culturas = []

# cálculo de insumos baseado na fonte http://

def calcular_area(tipo: str, base: float, altura: float):
    if tipo == "Cana-de-açúcar":
        return base * altura
    elif tipo == "Milho":
        return base * altura 
    else:
        return 'Digite um valor válido*'

def adicionar_cultura():
    print("\nCadastro de nova cultura:")
    tipo = input("Digite o tipo de cultura (Cana-de-açúcar ou Milho): ")
    
    if tipo not in ["Cana-de-açúcar", "Milho"]:
        print("🚨 Cultura inválida! Tente novamente.")
        return
    
    base = float(input("Digite a largura do terreno (em metros): "))
    altura = float(input("Digite o comprimento do terreno (em metros): "))
    area = calcular_area(tipo, base, altura)


    culturas.append({
        "Tipo": tipo,
        "Área": area,
    })
    print("\n✅ Cultura adicionada com sucesso!\n")

if __name__ == "__main__":
    adicionar_cultura()