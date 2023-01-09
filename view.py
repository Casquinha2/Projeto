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
                elif lista_jog ==[]:
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
                       Também sempre pode optar por usar as nossas grelhas pré-definidas.
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
                
                jog_jogo.append(opcao[1])
                jog_jogo.append(opcao[2])
                bubble_sort(jog_jogo)
                jogador1 = jog_jogo[0]
                idjog1 = 1
                jogador2 = jog_jogo[1]
                idjog2 = 2
                if opcao[3] == "Pequeno" or opcao[3] == "pequeno":
                    w = 5
                    h = 4
                    n = 3
                    grelha = criar_grelha(w, h)
                    print(f"""
                    Jogo iniciado entre {jogador1} e {jogador2}.""")
                elif opcao[3] == "Médio" or opcao[3] == "médio":
                    w = 7
                    h = 6
                    n = 4
                    grelha = criar_grelha(w, h)
                    print(f"""
                    Jogo iniciado entre {jogador1} e {jogador2}.""")
                elif opcao[3] == "grande" or opcao[3] == "Grande":
                    w = 11
                    h = 8
                    n = 6
                    grelha = criar_grelha(w, h)
                    print(f"""
                    Jogo iniciado entre {jogador1} e {jogador2}.""")
                elif opcao[3] == int:  #depois fica as regras de insucesso tamanho
                    if opcao[4] < (opcao[3]/2) or opcao[4] > opcao[3]:
                        print(f"""
                Dimensões de grelha invalidas.""")
                    elif opcao[5] < opcao[3]:
                        print("""
                Tamanho de sequência invalido.""")
                pass
                #falta a condição das peças especiais
            elif opcao[0] == "DJ":
                if jog_jogo == []:
                            print("""
                        Não existe jogo em curso.""")
                else:
                    print(f"""
                            {opcao[3]} por {opcao[4]}
                            {jogador1}
                            
                            {jogador2}
                            """)#falta adicionar tamanho e quantidade de peças especiais.
                    pass
            elif opcao[0] == "V":
                    for i in range(h):
                        print(grelha[i])
            elif opcao[0] == "CP":
                if grelha == "":
                    print("""
                    Não existe nenhum jogo em curso.""")
                elif opcao[1] not in jog_jogo:
                    print(f"""
                    O jogador {opcao[1]} não está a participar no jogo em curso.""")
                
                #falta elif das peças especiais

                elif int(opcao[3]) - 1 > w or int(opcao[3]) < 0:    #sem sentido, modificar com peças especiais
                    print("""
                    Posição irregular""")
                else:
                    if opcao[1] == jogador1:
                        tamanho = int(opcao[2])
                        grelha = colocar_peca(tamanho , h, grelha, idjog1)
                        
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
                        G - Gravar ficheiro
                        Voltar
                    """)
            opcao = input("""
                    Opção escolhida: """)
            if opcao == "L":
                pass
            elif opcao == "G":
                pass
            elif opcao == "Voltar":
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