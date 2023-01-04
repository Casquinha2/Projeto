from controller import *
def main():
    lista_jog = [] #jogadores registrados
    jog_jogo = [] #jogadores em jogo
    jog_regis = [] #só nomes sem pontuação
    print("""
    Bem vindo ao n em linha!
    """)
    while True:
        print(""" 
    Para começar, por favor selecione uma das seguintes opções:
        Como jogar
        Jogador
        Jogo
        Dados guardados
        Sair
        """)
        opcao = input("""
    Opção escolhida: """).lower()

        if opcao == "como jogar":
            print("""
        No jogo "n em linha" tu poderás definir tanto o tamanho das peças como o da grelha. 
        O jogo consiste em jogadas intercaladas entre os diversos jogadores.
        O objetivo é formar n em linha (em que n é o número de peças em linha necessárias para ganhar), 
        largando peças numa determinada posição da grelha. 
        Ou seja, o primeiro a fazer n em linha ganha!
        Este jogo também contém peças especiais em que poderás definir o tamanho destas e quantas poderás utilizar durante o jogo.
            """)
        elif opcao == "jogador":
            print("""
        Menu Jogador
            Por favor selecione uma das seguintes opções:
                RJ "nome" - Registrar Jogador
                EJ "nome" - Remover Jogador
                LJ - Lista de jogadores
                Voltar
            
            """)
            opcao = input("""
            Opção escolhida:""").split()

            if opcao[0] == "RJ":
                if opcao[1] not in lista_jog:
                    jogador = adicionar_jogador(opcao[1])
                    lista_jog.append(jogador)
                    jog_regis.append(opcao[1])   
                    print("""
                    Jogador registado com sucesso.""")
                else:
                    print("""
                    Jogador já existe.""")
            elif opcao[0] == "EJ":
                if opcao[1] in jog_regis and opcao[1] not in jog_jogo:
                    lista_jog = remover_jogador(opcao[1], lista_jog)
                    print("""
                    Jogador removido com sucesso.""")
                elif opcao[1] not in jog_regis:
                    print("""
                    Jogador ainda não foi registado.""")
                else:
                    print("""
                    O jogador está num jogo em curso.""")
            elif opcao[0] == "LJ":
                if lista_jog != "":
                    for i in range(0, len(lista_jog)):
                        print(lista_jog[i])
                else:
                    print("""
                    Não existem jogadores registados""")

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
                       Aqui deve indicar os nome dos dois jogadores; comprimento e altura da grelha de jogo;
                         tamanho da sequência para a vitória;
                         tamanho das peças especiais (pode usar a quantidade de peças que lhe apetecer).
                       Também sempre pode optar por usar as nossas grelhes pré-definidas.
                         Só precisa digitar os nomes do jogador e:
                           -Pequeno - Para uma grelha com dimenções 
                           -Médio - Para uma grelha com dimensões 
                           -Grande - Para uma grelha com as dimensões 
                DJ - Detalhes do Jogo
                V - Visualizar resultado
                CP - Colocar Peça "Nome" "Tamanho peça" "Posição" "Sentido"
                            (Não é preciso "sentido" para peças de tamanho 1).
                D - Desistir "Nome" "Nome"
                            (Segundo nome é opcional).
                Voltar
            """)
            opcao = input("""
            Opção escolhida: """).split()
            if opcao[0] == "IJ":
                if jog_jogo != []:
                    print("""
                Existe um jogo em curso neste momento.""")
                elif opcao[1] not in jog_regis:
                    print(f"""
                O jogador {opcao[1]} não se encontra registrado.""")
                elif opcao[2] not in jog_regis:
                    print(f"""
                O jogador {opcao[2]} não se encontra registrado.""")
                
                pass #faltam algumas saidas com insucesso e fazer o jogo em si (mas o jogo é no "else")
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
        Menu Dados guardados
            Por favor selecione uma das seguintes opções:
                L - Ler ficheiro
                G- Gravar ficheiro
            """)
            opcao = input("""
            Opção escolhida: """).split()
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
            sair = input("""
        Tem a certeza que quer sair? """).lower()
            if sair == "sim":
                guardar = input(""" 
            Deseja guardar os ficheiros antes de sair?
                """).lower()
                if guardar == "sim":
                    print("""
                Os seus dados foram guardados.
                Esperemos que volte em breve. \N{loudly crying face}
                    """)
                elif guardar == "nao" or guardar == "não":
                    print("""
                Os seus ficheiros não foram guardados.
                Esperemos que volte em breve. \N{loudly crying face}
                    """)
                else:
                    print("""
                A expressão introduzida não tem nada haver com a pergunta.
                Por isso vamos guardar os seus dados.
                Esperemos que volte em breve. \N{loudly crying face}
                    """)
                    
                break
            elif sair == "não" or sair =="nao":
                continue
            else:
                print("""
            A expressão introduzida não tem nada haver com a pergunta.
            Por isso vou considerar como um não. \U0001F606 """) 

        else:
            print("""
        A expressão introduzida deve estar mal escrita. Por favor tente de novo. """)