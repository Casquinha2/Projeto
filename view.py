from controller import *
from model import *
def main():
    lista_jog = [] #jogadores registrados
    jog_jogo = [] #jogadores em jogo
    grelha = []
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
                    print("""
                    Jogador registado com sucesso.""")
                else:
                    print("""
                    Jogador já existe.""")
            elif opcao[0] == "EJ":
                verifica = verificar_jogador(lista_jog, opcao[1])
                if grelha != []:
                    print("""
                    O jogador está num jogo em curso.""")
                elif verifica == False:
                    print("""
                    Jogador ainda não foi registado.""")
                else:
                    lista_jog = remover_jogador(opcao[1], lista_jog)
                    print("""
                    Jogador removido com sucesso.""")
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
                verifica1 = verificar_jogador(lista_jog, opcao[1])
                verifica2 = verificar_jogador(lista_jog, opcao[2])
                if jog_jogo != []:
                    print("""
                Existe um jogo em curso neste momento.""")
                elif verifica1 == False:
                    print(f"""
                O jogador {opcao[1]} não se encontra registado.""")
                elif verifica2 == False:
                    print(f"""
                O jogador {opcao[2]} não se encontra registado.""")
                else:
                    
                    jog_jogo.append(opcao[1])
                    jog_jogo.append(opcao[2])
                    bubble_sort(jog_jogo)
                    
                    if opcao[3] == "Pequeno" or opcao[3] == "pequeno" or opcao[3] == "PEQUENO":
                        w = 5
                        h = 4
                        n = 3
                        grelha = criar_grelha(w, h)
                        print(f"""
                        Jogo iniciado entre {jog_jogo[0]} e {jog_jogo[1]}.""")
                    elif opcao[3] == "Médio" or opcao[3] == "médio" or opcao[3] == "MÉDIO":
                        
                        w = 7
                        h = 6
                        n = 4
                        lista_especiais = adicionar_pecas_especiais(opcao)
                        
                        ver_esp = verificar_especiais(lista_especiais, n)
                        
                        if ver_esp == False:
                            print("""
                    Dimensão das peças especiais são inválidas""")
                        else:
                            grelha = criar_grelha(w, h)
                            print(f"""
                        Jogo iniciado entre {jog_jogo[0]} e {jog_jogo[1]}.""")
                    elif opcao[3] == "grande" or opcao[3] == "Grande" or opcao[3] == "GRANDE":
                        w = 11
                        h = 10
                        n = 6
                        grelha = criar_grelha(w, h)
                        print(f"""
                        Jogo iniciado entre {jog_jogo[0]} e {jog_jogo[1]}.""")
                    elif opcao[3] != "":  #depois fica as regras de insucesso tamanho
                        w = int(opcao[3])
                        h = int(opcao[4])
                        n = int(opcao[5])
                        lista_especiais = adicionar_pecas_especiais_custom(opcao)
                        ver_esp = verificar_especiais(lista_especiais, n)
                        if h < w / 2 or h > w:
                            print(f"""
                    Dimensões de grelha invalidas.""")
                        elif n > w:
                            print("""
                    Tamanho de sequência invalido.""")
                        elif ver_esp == False:
                            print("""
                    Dimensão das peças especiais são inválidas""")
                        else:
                            grelha = criar_grelha(w, h)
                            print(f"""
                        Jogo iniciado entre {jog_jogo[0]} e {jog_jogo[1]}.""")
            elif opcao[0] == "DJ":
                if jog_jogo == []:
                            print("""
                        Não existe jogo em curso.""")
                else:
                    print(f"""
                            {len(grelha[0])} por {len(grelha)}
                            {jog_jogo[0]}
                            
                            {jog_jogo[1]}
                            """)#falta adicionar tamanho e quantidade de peças especiais.
                    pass
            elif opcao[0] == "V":
                print("\n")
                for linha in grelha:
                    print(' '.join(linha))
                print('\n')
                
            elif opcao[0] == "CP":
                if grelha == "":
                    print("""
                    Não existe nenhum jogo em curso.""")
                elif opcao[1] not in jog_jogo:
                    print(f"""
                    O jogador {opcao[1]} não está a participar no jogo em curso.""")
                
                #falta elif das peças especiais

                elif int(opcao[3]) - 1 > len(grelha[0]) or int(opcao[3]) < 0:    #sem sentido, modificar com peças especiais
                    print("""
                    Posição irregular""")
                else:
                    if int(opcao[2]) == 1:
                        if opcao[1] == jog_jogo[0]:
                            peca = int(opcao[3]) - 1
                            grelha = colocar_peca(peca , grelha, len(grelha), "X")
                        else:
                            peca = int(opcao[3]) - 1
                            grelha = colocar_peca(peca , grelha, len(grelha), "O")
                            vitoria = verificar_vitoria_horizontal(grelha, len(grelha[0]), len(grelha), n)
                            if vitoria == True:
                                print("1")
                                print(f"O jogador {opcao[1]} ganhou!")
                                grelha = []
                                jog_jogo = []
                            else:
                                vitoria = verificar_vitoria_vertical(grelha, len(grelha[0]), len(grelha), n)
                                if vitoria == True:
                                    print("2")
                                    print(f"O jogador {opcao[1]} ganhou!")
                                    grelha = []
                                    jog_jogo = []
                                else:
                                    vitoria = verificar_vitoria_diagonal_baixo(grelha, len(grelha[0]), len(grelha), n)
                                    if vitoria == True:
                                        print("3")
                                        print(f"O jogador {opcao[1]} ganhou!")
                                        grelha = []
                                        jog_jogo = []
                                    else:
                                        vitoria = verificar_vitoria_diagonal_cima(grelha, len(grelha[0]), len(grelha), n)                    
                                        if vitoria == True:
                                            print("4")
                                            print(f"O jogador {opcao[1]} ganhou!")
                                            grelha = []
                                            jog_jogo = []
                                        else:
                                            continue
                                            
                    else:
                        pass
                        #Fazer uma nova função para colocar peças especiais
                            
            elif opcao[0] == "D":
                if opcao[2] == "":
                    if opcao[1] not in lista_jog:
                        print(f"""
                    O jogador {opcao[1]} não está registado..""")
                    elif jog_jogo == []:
                        print("""
                    Não existe um jogo em curso.""")
                    elif opcao[1] not in jog_jogo:
                        print(f"""
                    O jogador {opcao[1]} não participa no jogo em curso.""")
                    else:
                        jog_jogo = []
                        grelha = []
                        lista_jog = adicionar_pontos_1(lista_jog, opcao[1], jog_jogo)
                else:
                    if opcao[1] not in lista_jog:
                        print(f"""
                    O jogador {opcao[1]} não está registado.""")
                    elif opcao[2] not in lista_jog:
                        print(f"""
                    O jogador {opcao[2]} não está registado.""")
                    elif jog_jogo == []:
                        print("""
                    Não existe um jogo em curso.""")
                    elif opcao[1] not in jog_jogo:
                        print(f"""
                    O jogador {opcao[1]} não participa no jogo em curso.""")
                    elif opcao[2] not in jog_jogo:
                        print(f"""
                    O jogador {opcao[2]} não participa no jogo em curso.""")
                    else:
                        lista_jog = adicionar_pontos_2(lista_jog, opcao[1], jog_jogo)
                        lista_jog = adicionar_pontos_2(lista_jog, opcao[2], jog_jogo)
                        jog_jogo = []
                        grelha = []
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
                    Opção escolhida: """).split()
            if opcao[0] == "L":
                ficheiro = ler_ficheiro_json(opcao[1])
                if ficheiro[1] != []:
                    lista_jog = ficheiro[0]
                    grelha = ficheiro[1]
                    jog_jogo = ficheiro[2]
                    n = ficheiro[3][0]
                    lista_especiais = ficheiro[4]
                else:
                    lista_jog = ficheiro[0]
            elif opcao[0] == "G":
                if jog_jogo != []:
                    escrever_ficheiro_json(opcao[1], lista_jog, grelha, jog_jogo, n, lista_especiais)
                else:
                    escrever_ficheiro_json_sgrelha(opcao[1], lista_jog)
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
                    nome_ficheiro = input("""
                    Coloque aqui o nome que quer para o ficheiro: """)
                    escrever_ficheiro_json(nome_ficheiro, lista_jog, grelha, jog_jogo, n, lista_especiais)
                    print("""
                        Os seus dados foram guardados.
                        Esperemos que volte em breve. \N{loudly crying face}
                            """)
                    break
                elif guardar == "nao" or guardar == "não":
                    print("""
                        Os seus ficheiros não foram guardados.
                        Esperemos que volte em breve. \N{loudly crying face}
                            """)
                    break
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