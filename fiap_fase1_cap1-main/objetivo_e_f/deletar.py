from objetivo_e_f.utils_deletar import deletar_formato_cultura
from objetivo_a.culturas import CULTURA_1, CULTURA_2
from objetivo_d.vetor_de_dados import Culturas


# Função para deletar dados
def deletar_dados(culturas:Culturas):
    print("\nEscolha a cultura para deletar dados:")
    cultura_nome = input(f""" 
 0 - VOLTAR AO MENU
 1 - {CULTURA_1}
 2 - {CULTURA_2}
    """).strip().lower()
    
    # Mapeia as escolhas para as chaves do dicionário
    if cultura_nome == '0' or cultura_nome == 'voltar ao menu':
        return

    if cultura_nome == '1':
        cultura_nome = CULTURA_1

    elif cultura_nome == '2':
        cultura_nome = CULTURA_2

    else:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    
    print(f"Você escolheu a {cultura_nome} para deletar os dados.")
    if cultura_nome == CULTURA_1:
        deletar_formato_cultura(culturas, CULTURA_1)
    elif cultura_nome == CULTURA_2:
        deletar_formato_cultura(culturas, CULTURA_2)