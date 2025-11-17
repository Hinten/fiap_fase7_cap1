from objetivo_e_f.apresentacao_de_dados import apresentacao_de_dados
from objetivo_e_f.utils_menu import input_float
from objetivo_e_f.utils_menu import calcular_manejo
from objetivo_a.culturas import CULTURA_1, CULTURA_2
from objetivo_d.vetor_de_dados import Culturas


# Função para entrada de dados de cultura
def entrada_dados(culturas:Culturas):
    print("\nEntrada de Dados:")
    cultura_nome = input(f"""
 0 - VOLTAR AO MENU
 1 - {CULTURA_1}
 2 - {CULTURA_2}
    """).strip().lower()
    
    if cultura_nome in ('0', 'voltar ao menu', 'voltar'):
        print ("Retornando ao menu principal.")
        return
    if cultura_nome not in {'1', CULTURA_1, '2', CULTURA_2}:
        print("Cultura não reconhecida. Retornando ao menu.")
        return

    if cultura_nome in {'1', CULTURA_1}:
        cultura_nome = CULTURA_1

    elif cultura_nome in {'2', CULTURA_2}:
        cultura_nome = CULTURA_2

    #todo verificar o tipo de área por cultura e chamar a função correta
    def entrada_formato():# Função para entrada de formato do plantio (dentro de entrada_dados)
        print("\nEscolha a forma do seu terreno:")
        forma_nome = input("""
    0 - VOLTAR 
    1 - Retangular
    2 - Triangular
        """).strip().lower()
        
        if forma_nome in ('0', 'voltar'):
            print("Retornando ao menu principal.")
            return None  # Retorna None para indicar que o usuário cancelou
        if forma_nome not in {'1', 'retangular', '2', 'triangular'}:
            print("Formato não reconhecido. Retornando à seleção de culturas.")
            return None
        if forma_nome in {'1', 'retangular'}:
            print('Você escolheu o plantio Retangular.')
            altura = input_float('Digite as dimensões do primeiro lado: ')
            base = input_float('Digite as dimensões do segundo lado: ')
            area = base * altura

            if cultura_nome == CULTURA_1:
                culturas.append_area_cultura_1(tipo='1', base=base, altura=altura)
            else:
                culturas.append_area_cultura_2(tipo='1', base=base, altura=altura)


        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = input_float('Digite a altura do triângulo: ')
            base = input_float('Digite a base do triângulo: ')
            area = (base * altura) / 2

            if cultura_nome == CULTURA_1:
                culturas.append_area_cultura_1(tipo='2', base=base, altura=altura)
            else:
                culturas.append_area_cultura_2(tipo='2', base=base, altura=altura)

        print(f'A área do plantio é: {area:.2f}m²')
        return area  # Retorna a área calculada

    # Capturar a área do terreno
    area = entrada_formato()
    if area is None:  # Se o usuário cancelou, volta ao menu
        return

    # Calcular o manejo de insumo automaticamente com base na cultura e na área

    print(f"Dados de {cultura_nome} registrados com sucesso.")
    print(apresentacao_de_dados(cultura_nome, area))
