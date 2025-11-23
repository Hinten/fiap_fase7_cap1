from objetivo_e_f.entrada_dados import entrada_dados # Importando a função de entrada de dados
from objetivo_d.vetor_de_dados import Culturas
from objetivo_e_f.saida_dados import saida_dados # Importando a função de saída de dados
from objetivo_e_f.atualizar import atualizar_dados # Importando a função de atualização de dados
from objetivo_e_f.deletar import deletar_dados # Importando a função de deleção de dados

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Opções:")
    print("1 - Entrada de Dados")
    print("2 - Saída de Dados")
    print("3 - Atualizar Dados")
    print("4 - Deletar Dados")
    print("0 - Sair do Programa")

# Função principal para gerenciar o menu
def main():

    culturas = Culturas.new_or_from_file()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-4 ou 'Sair'): ").strip().lower()

        if escolha in {'1', 'entrada','Entrada de Dados', 'entrada de dados', 'entrar'}:
            entrada_dados(culturas)
        elif escolha in {'2', 'saída','saida de dados', 'Saída de Dados'}:
            saida_dados(culturas)
        elif escolha in {'3', 'atualizar', 'atualizar dados'}:
            atualizar_dados(culturas)
        elif escolha in {'4', 'deletar', 'deletar dados'}:
            deletar_dados(culturas)
        elif escolha in {'0', 'sair', 'sair do programa', 'fechar'}:
            print("\n Tem certeza que deseja sair?")
            sair = input(f"""
 1 - Sim
 2 - Não
    """).strip().lower()
            if sair in ['1', 'sim', 's']:
                print("Saindo do Programa...")
                break
            elif sair in ['2', 'nao', 'não', 'n']:
                print("Retornando ao menu...")
            else:
                print("Resposta inválida. Retornando ao menu...")
        else:
            print("Opção inválida. Tente novamente.")

# Executando o programa
if __name__ == "__main__":
    main()
