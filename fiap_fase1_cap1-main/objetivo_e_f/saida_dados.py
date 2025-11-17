from objetivo_a.culturas import CULTURA_1, CULTURA_2
from objetivo_d.vetor_de_dados import Culturas
from objetivo_e_f.apresentacao_de_dados import apresentacao_de_dados


# Função para saída de dados
def saida_dados(culturas: Culturas):
    print("\nSaída de Dados:")
    cultura_nome = input(f"""
 0 - VOLTAR AO MENU
 1 - {CULTURA_1}
 2 - {CULTURA_2}
    """).strip().lower()
    
    if cultura_nome == '0' or cultura_nome == 'voltar ao menu':
        return
    if cultura_nome not in {'1', 'CULTURA_1', '2', 'CULTURA_2'}:
        print("Cultura não reconhecida. Retornando ao menu.")
        return

    if cultura_nome in {'1', 'CULTURA_1'}:
        cultura_nome = CULTURA_1
    elif cultura_nome in {'2', 'CULTURA_2'}:
        cultura_nome = CULTURA_2
    else:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    
    print(f"\nDados para {cultura_nome}:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"Registro {i}: Área = {dado}")
            print(f"{apresentacao_de_dados(cultura_nome, dado.calcular_area())}")
