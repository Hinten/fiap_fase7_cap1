from objetivo_a.culturas import CULTURA_1, CULTURA_2
from objetivo_d.vetor_de_dados import Culturas
from objetivo_e_f.utils_menu import input_int


# Função para deletar um dado específico dentro de cada cultura
def deletar_formato_cultura(culturas:Culturas, cultura_nome):
    print("\nEscolha o registro para deletar:")
    if len(culturas[cultura_nome]) == 0 or not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
        return
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado}")
    
    # Solicita o índice antes de confirmar
    indice = input_int(f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser deletado (1 a {len(culturas[cultura_nome])}): ")
    
    if indice == 0:
        print("Retornando ao menu principal.")
        return

    if indice < 1 or indice > len(culturas[cultura_nome]):
        print("Índice inválido.")
        return
    
    print(f"Você escolheu deletar o registro {indice}. Tem certeza?")
    confirmacao = input("""
    0 - NÃO
    1 - SIM
    """).strip().lower()
    
    # Verificação de confirmação
    if confirmacao in ('0', 'não', 'nao', 'n', 'no', 'NÃO', 'NAO', 'N', 'NO'):
        print("Operação cancelada. Retornando ao menu.")
        return  # Cancela a operação
    elif confirmacao == '1' or confirmacao == 'sim':

        if cultura_nome == CULTURA_1:
            culturas.remove_area_cultura_1(indice - 1)
        elif cultura_nome == CULTURA_2:
            culturas.remove_area_cultura_2(indice - 1)
        else:
            print("Cultura não reconhecida. Retornando ao menu.")


        print(f"Registro {indice} deletado com sucesso.")
