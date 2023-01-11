def adicionar_jogador(nome):
    dicionario = {"jogador": nome, "jogos": 0, "Pontos": 0}
    return dicionario

def remover_jogador(nome, lista):
    for i in lista:
        jogador = i.get("jogador")
        if jogador == nome:
            lista.remove(i)
            return lista

def criar_grelha(w, h):
    grelha = []
    lista = []
    for i in range(w):
        lista.append("_")
    for j in range(h):
        grelha.append(lista)
    return grelha

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp


def colocar_peca(peca, grelha, h, jog):
    for i in range(h - 1, 0 , -1):
        if grelha[i,peca] != "_":
            continue
        else:
            grelha[i,peca] = jog
            break
    return grelha

def verificar_vitoria_horizontal(grelha, w, h, n):
    m = 0
    for j in range(h):
        for k in range(w - 1):
            if grelha [j, k] != 0:
                if grelha[j, k] == grelha[j, k + 1]:
                    m += 1
                else:
                    m = 0
    if m == n:
        return True
    else:
        return False

def verificar_vitoria_vertical(grelha, w, h, n):
    m = 0
    for j in range(h - 1):
        for k in range(w):
            if grelha [j, k] != 0:
                if grelha[j, k] == grelha[j + 1, k]:
                    m += 1
                else:
                    m = 0
    if m == n:
        return True
    else:
        return False
    
def verificar_vitoria_diagonal_baixo(grelha, w, h, n):
    m = 0
    for j in range(h - 1):
        for k in range(w - 1):
            if grelha [j, k] != 0:
                if grelha[j, k] == grelha[j + 1, k + 1]:
                    m += 1
                else:
                    m = 0
    if m == n:
        return True
    else:
        return False

def verificar_vitoria_diagonal_cima(grelha, w, h, n):
    m = 0
    for j in range(h - 1):
        for k in range(1, w):
            if grelha [j, k] != 0:
                if grelha[j, k] == grelha[j -1 , k - 1]:
                    m += 1
                else:
                    m = 0
    if m == n:
        return True
    else:
        return False

def verificar_vitoria_diagonal_baixo():
    pass

def adicionar_pecas_especiais(opcao):
    n = 0
    lista = []
    while opcao[n] != "":
        n+1
    for i in range(6, n + 1):
        temp = int(opcao[i])
        lista.append(temp)
    return lista

def verificar_especiais(lista, n):
    for i in lista:
        if i >= n:
            return False
    return True

