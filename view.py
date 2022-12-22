from controller import *
import emoji
def main():
    lista_jog = []
    print("""
    Bem vindo ao n em linha!
    """)
    while True:
        print(""" 
    Para começar, por favor selecione uma das seguintes opções:
        Regras
        Jogador
        Jogo
        Dados guardados
        Sair
        """) #colocar opções jogador, jogo, dados guardados, sair
        opcao = input("Opção escolhida 1: ").lower()

        if opcao == "regras":
            print("""
            
            """)

        elif opcao == "jogador":
            print("""
            Menu Jogador
            Por favor selecione uma das seguintes opções:
                RJ - Registrar Jogador
                EJ - Remover Jogador
                LJ - Lista de jogadores
                Voltar
            
            """) #colocar RJ, EJ, LJ
            opcao = input("Opção escolhida 2:").split()

            if opcao[0] == "RJ":
                if opcao[1] not in lista_jog:
                    lista_jog.append(adicionar_jogador(opcao[1]))   
                print(lista_jog)
            elif opcao[0] == "EJ":
                if opcao[1] in lista_jog:
                    lista_jog.remove(opcao[1])
            elif opcao[0] == "LJ":
                for i in range(0, len(lista_jog)):
                    print(lista_jog[i])
            elif opcao[0] == "Voltar":
                continue
            else:
                print("""
                A expressão introduzida deve estar mal escrita. Por favor tente de novo.""")

        elif opcao == "jogo":
            print("""
            Menu Jogo
            Por favor selecione uma das seguintes opções:
                IJ - Iniciar Jogo
                DJ - Detalhes do Jogo
                V - Visualizar resultado
                CP - Colocar Peça
                D - Desistir
                Voltar
            """) #colocar IJ, DJ, V, CP, D
            opcao = input("Opção escolhida 2: ").split()
            if opcao[0] == "IJ":
                #ter grelhas pré-definidas por nós
                pass
            elif opcao[0] == "DJ":
                pass
            elif opcao[0] == "V":
                pass
            elif opcao[0] == "CP":
                pass
            elif opcao[0] == "D":
                pass
            elif opcao[0] == "Voltar":
                continue
            else:
                print("""
                A expressão introduzida deve estar mal escrita. Por favor tente de novo.""")

        elif opcao == "dados guardados":
            print("""
            """) #colocar L, G
            opcao = input("Opção escolhida 2: ").split()
            if opcao == "L":
                pass
            elif opcao == "G":
                pass
            elif opcao[0] == "Voltar":
                continue
            else:
                print("""
                A expressão introduzida deve estar mal escrita. Por favor tente de novo.""")

        elif opcao == "sair":
            print("""
            """) #perguntar se quer sair
            sair = input("Tem a certeza que quer sair? ").lower()
            if sair == "sim":
                print(""" \N{loudly crying face}
                """) #despedida usar este emoji \N{loudly crying face}
                break
            elif sair == "não" or sair =="nao":
                continue
            else:
                print("""
                A expressão introduzida não tem nada haver com a pergunta, vou considerar isso como um não. \U0001F606 """) 

        else:
            print("""
            A expressão introduzida deve estar mal escrita. Por favor tente de novo. """)