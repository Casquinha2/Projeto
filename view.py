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
                        lista_especiais = adicionar_pecas_especiais(opcao)                        
                        ver_esp = verificar_especiais(lista_especiais, n)
                        lista_especiais1, lista_especiais2 = duplicar_especiais(lista_especiais)                        
                        if ver_esp == False:
                            print("""
                Dimensão das peças especiais são inválidas""")
                        else:
                            grelha = criar_grelha(w, h)
                            print(f"""
                Jogo iniciado entre {jog_jogo[0]} e {jog_jogo[1]}.""")
                    elif opcao[3] == "Médio" or opcao[3] == "médio" or opcao[3] == "MÉDIO":                        
                        w = 7
                        h = 6
                        n = 4
                        lista_especiais = adicionar_pecas_especiais(opcao)                       
                        ver_esp = verificar_especiais(lista_especiais, n)
                        lista_especiais1, lista_especiais2 = duplicar_especiais(lista_especiais)
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
                        lista_especiais = adicionar_pecas_especiais(opcao)
                        ver_esp = verificar_especiais(lista_especiais, n)
                        lista_especiais1, lista_especiais2 = duplicar_especiais(lista_especiais)
                        if ver_esp == False:
                            print("""
                Dimensão das peças especiais são inválidas""")
                        else:
                            grelha = criar_grelha(w, h)
                            print(f"""
                    Jogo iniciado entre {jog_jogo[0]} e {jog_jogo[1]}.""")
                    elif opcao[3] != "":
                        w = int(opcao[3])
                        h = int(opcao[4])
                        n = int(opcao[5])
                        lista_especiais = adicionar_pecas_especiais_custom(opcao)
                        ver_esp = verificar_especiais(lista_especiais, n)
                        lista_especiais1, lista_especiais2 = duplicar_especiais(lista_especiais)
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
                    dic_especiais1 = passar_especial_dic(lista_especiais1)
                    dic_especiais2 = passar_especial_dic(lista_especiais2)
                    print(f"""
                {len(grelha[0])} de comprimento por {len(grelha)} de largura
                            Jogador:
                                {jog_jogo[0]}""")
                    for i in dic_especiais1:
                        j = dic_especiais1.get(i)
                        print(f"""
                        Peças especiais de {i} : {j}""")
                    print("\n")
                    print(f"""
                            Jogador:
                                {jog_jogo[1]}""")
                    for i in dic_especiais2:
                        j = dic_especiais2.get(i)
                        print(f"""
                        Peças especiais de {i} : {j}""")
            elif opcao[0] == "V":
                print("\n")
                for linha in grelha:
                    print(' '.join(linha))
                print('\n')
                
            elif opcao[0] == "CP":
                if opcao[1] == lista_jog[0]:
                    especiais = verificar_tamanho_especiais(lista_especiais1, opcao)
                else:
                    especiais = verificar_tamanho_especiais(lista_especiais2, opcao)
                
                if grelha == []:
                    print("""
                Não existe nenhum jogo em curso.""")
                elif opcao[1] not in jog_jogo:
                    print(f"""
                O jogador {opcao[1]} não está a participar no jogo em curso.""")
                elif especiais == False:
                    print("""
                Tamanho de peça não disponivel.""")
                elif opcao[4].lower == "direita":
                    if 0 >= opcao[2] + opcao[3] and opcao[2] + opcao[3] >= len(grelha) + 1:
                        print("""
                Posição irregular.""")
                elif opcao[4].lower == "esquerda":
                    if 0 >= opcao[2] - opcao[3] and opcao[2] - opcao[3] >= len(grelha) + 1:
                        print("""
                Posição irregular.""")
                else:
                    if opcao[4].lower == "direita":
                        d = opcao[2]
                        f = 1
                    elif opcao[4].lower == "esquerda":
                        d = -opcao[2]
                        f = -1
                    else:
                        print("""
                Sentido inválido.""")
                    for i in range(0, d, f):
                        if opcao[1] == jog_jogo[0]:
                            wpeca = int(opcao[3]) - 1 + i
                            grelha, hpeca = colocar_peca(wpeca , grelha, len(grelha), "X")
                            vitoria = verificar_vitoria_horizontal(grelha, len(grelha[0]), len(grelha), n)
                            if vitoria == True:
                                print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                grelha = []
                                jog_jogo = []
                                
                            else:
                                vitoria = verificar_vitoria_vertical(grelha, len(grelha[0]), len(grelha), n)
                                if vitoria == True:
                                    print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                    lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                    grelha = []
                                    jog_jogo = []
                                    
                                else:
                                    vitoria = verificar_vitoria_diagonal_baixo(grelha, wpeca, hpeca, n, "X")
                                    if vitoria == True:
                                        print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                        lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                        grelha = []
                                        jog_jogo = []
                                        
                                    else:
                                        vitoria = verificar_vitoria_diagonal_cima(grelha, wpeca, hpeca, n, "X")                    
                                        if vitoria == True:
                                            print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                            lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                            grelha = []
                                            jog_jogo = []
                                            
                        elif opcao[1] == jog_jogo[1]:
                            wpeca = int(opcao[3]) - 1
                            grelha, hpeca = colocar_peca(wpeca , grelha, len(grelha), "O")
                            vitoria = verificar_vitoria_horizontal(grelha, len(grelha[0]), len(grelha), n)
                            if vitoria == True:
                                print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                grelha = []
                                jog_jogo = []
                                
                            else:
                                vitoria = verificar_vitoria_vertical(grelha, len(grelha[0]), len(grelha), n)
                                if vitoria == True:
                                    print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                    lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                    grelha = []
                                    jog_jogo = []
                                    
                                else:
                                    vitoria = verificar_vitoria_diagonal_baixo(grelha, wpeca, hpeca, n, "O")
                                    if vitoria == True:
                                        print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                        lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                        grelha = []
                                        jog_jogo = []
                                        
                                    else:
                                        vitoria = verificar_vitoria_diagonal_cima(grelha, wpeca, hpeca, n, "O")                   
                                        if vitoria == True:
                                            print(f"""
                    O jogador {opcao[1]} ganhou!""")
                                            lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                                            grelha = []
                                            jog_jogo = []
                                            
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
                        lista_jog = adicionar_jogos_1(lista_jog, opcao[1], jog_jogo)
                        jog_jogo = []
                        grelha = []
                        
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
                        lista_jog = adicionar_jogos_2(lista_jog, opcao[1], jog_jogo)
                        lista_jog = adicionar_jogos_2(lista_jog, opcao[2], jog_jogo)
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
                    lista_especiais1 = ficheiro[4]
                    lista_especiais2 = ficheiro[5]
                else:
                    lista_jog = ficheiro[0]
            elif opcao[0] == "G":
                if jog_jogo != []:
                    listan = [n]
                    escrever_ficheiro_json(opcao[1], lista_jog, grelha, jog_jogo, listan, lista_especiais1, lista_especiais2)
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
                    A expressão introduzida deve estar mal escrita.
                    Por isso vou considerar como um não. \U0001F606 """) 

        else:
            print("""
                A expressão introduzida deve estar mal escrita. Por favor tente de novo. """)