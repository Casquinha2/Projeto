def adicionar_jogador(nome):
    dicionario = {"Jogador": nome, "Pontos": 0, "Jogos": 0}
    return dicionario

def remover_jogador(nome, lista):
    for i in lista:
        jogador = i.get("Jogador")
        if jogador == nome:
            lista.remove(i)
            return lista

def criar_grelha(w, h):
    grelha = []
    for j in range(h):
        linha = []
        for i in range(w):
            linha.append("_")
        grelha.append(linha)
    return grelha

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp


def colocar_peca(peca, grelha, h, jog):
    for i in range(h-1, 0, -1):
        if grelha[i][peca] != "_":
            print("1")    
            continue
        else:
            print("2")
            grelha[i][peca] = jog
            print (grelha)
            break
    return grelha

def verificar_vitoria_horizontal(grelha, w, h, n):
    m = 0
    for j in range(h - 1, - 1, - 1):
        for k in range(w - 1):
            if grelha [j][k] != "_":
                if grelha[j][k] == grelha[j][k + 1]:
                    m += 1
                    if m + 1 == n:
                        return True
                else:
                    m = 0

def verificar_vitoria_vertical(grelha, w, h, n):
    m = 0
    for k in range(w):
        for j in range(h - 1, 0, -1):
            if grelha [j][k] != "_":
                if grelha[j][k] == grelha[j - 1][k]:
                    m += 1
                    if m + 1 == n:
                        return True
                else:
                    m = 0
    
def verificar_vitoria_diagonal_baixo(grelha, w, h, n):
    m = 0                                                #horizontal
    for j in range(h - 1, - 1, - 1):
        for k in range(w - 1):
            if grelha [j][k] != "_":
                if grelha[j][k] == grelha[j][k + 1]:
                    m += 1
    p = 0                                                #vertical
    for k in range(w):
        for j in range(h - 1, 0, -1):
            if grelha [j][k] != "_":
                if grelha[j][k] == grelha[j - 1][k]:
                    p += 1
                    if p + 1 == n and m + 1 == n:
                        return True


def verificar_vitoria_diagonal_cima(grelha, w, h, n):
    m = 0
    for j in range(h - 1, 0, -1):
        for k in range(0, w):
            if grelha [j][k] != "_":
                if grelha[j][k] == grelha[j - 1][k  + 1]:
                    m += 1
                    if m + 1 == n:
                        return True
                else:
                    m = 0

def adicionar_pecas_especiais_custom(opcao):
    n = len(opcao)
    lista = []
    if n > 6:
        if opcao[6] != "":
            for i in range(6, n + 1):
                temp = int(opcao[i])
                lista.append(temp)
    return lista

def adicionar_pecas_especiais(opcao):
    n = len(opcao)
    lista = []
    if n > 4:
        for i in range(4, n + 1):
            print(i)
            print(opcao[i])
            temp = int(opcao[i])
            lista.append(temp)
    return lista

def verificar_especiais(lista, n):
    for i in lista:
        if i >= n:
            return False
        elif n == []:
            return False
    return True

def adicionar_pontos_1(lista, nome, jog_jogo):
    jog_jogo.remove(nome)
    vitorioso = jog_jogo[0]
    for i in lista:
        if nome in i:
            jogos = i.pop("Jogos")
            jogos += 1
            dic = {"Jogos": jogos}
            lista.update(dic)
            break
    for i in lista:
        if vitorioso in i:
            pontos = i.pop("Pontos")
            jogos = i.pop("Jogos")
            pontos += 1
            jogos += 1
            dic = {"Pontos": pontos, "Jogos": jogos}
            lista.update(dic)
            break
    return lista

def adicionar_pontos_2(lista, nome):
    for i in lista:
        if nome in i:
            jogos = i.pop("Jogos")
            jogos += 1
            dic = {"Jogos": jogos}
            lista.update(dic)
            break
    return lista
    
def verificar_jogador(lista, jogador):
    for i in lista:
        nome = i.get("Jogador")
        if nome == jogador:
            return True
    return False