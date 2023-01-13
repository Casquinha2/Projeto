def adicionar_jogador(nome):
    dicionario = {"Jogador": nome, "Pontos": 0, "Jogos": 0}
    return dicionario

def remover_jogador(n_jogador, lista):
    for jogador in lista:
        if jogador["Jogador"] == n_jogador:
            lista.remove(jogador)
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


def colocar_peca(wpeca, grelha, h, jog):
    for i in range(h - 1, -1, -1):
        if grelha[i][wpeca] != "_":
            validacao = False   
            continue
        else:
            grelha[i][wpeca] = jog
            validacao = True
            break
    return validacao, grelha, i

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
    
def verificar_vitoria_diagonal_baixo(grelha, wpeca, hpeca, n, jog):
    m = 0
    for linha in range(-wpeca+1, wpeca, 1):
        if 0 <= hpeca - linha < len(grelha) and 0 <= wpeca + linha < len(grelha):
            if grelha[hpeca - linha][wpeca + linha] == jog:
                m += 1
            else:
                m = 0    
        if m == n:
            return True
    
def verificar_vitoria_diagonal_cima(grelha, wpeca, hpeca, n, jog):
    r = 0
    for linha in range(-wpeca+1, wpeca, 1):
        if 0 <= hpeca + linha < len(grelha) and 0 <= wpeca + linha < len(grelha):
            if grelha[hpeca + linha][wpeca + linha] == jog:
                r += 1
            else:
                r = 0    
        if r == n:
            return True

def adicionar_pecas_especiais_custom(opcao):
    n = len(opcao)
    lista = []
    if n > 6:
        if opcao[6] != "":
            for i in range(6, n):
                temp = int(opcao[i])
                lista.append(temp)
    return lista

def adicionar_pecas_especiais(opcao):
    n = len(opcao) - 1
    lista = []
    if n > 3:
        for i in range(4, n + 1):
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

def adicionar_jogos_1(lista, nome, jog_jogo):
    jog_jogo.remove(nome)
    vitorioso = jog_jogo[0]
    for jogador in lista:
        if jogador["Jogador"] == nome:
            jogador["Jogos"] += 1 
            
    for jogador in lista:
        if jogador["Jogador"] == vitorioso:
            jogador["Jogos"] += 1 
            jogador["Pontos"] += 1
    return lista
            

def adicionar_jogos_2(lista, nome):
    for jogador in lista:
        if jogador["Jogador"] == nome:
            jogador["Jogos"] += 1 
    return lista
    
def verificar_jogador(lista, n_jogador):
    for jogador in lista:
        if jogador["Jogador"] == n_jogador:
            return True
    return False

def duplicar_especiais(lista_especiais):
    lista_especiais1 = lista_especiais
    lista_especiais2 = lista_especiais
    return lista_especiais1, lista_especiais2

def passar_especial_dic(lista_especiais):
    dic = {}
    for i in lista_especiais:
        if i not in dic:
            dictemp = {i: 1}
            dic.update(dictemp)
        else:
            m = dic.pop(i)
            dictemp = {i: m + 1}
            dic.update(dictemp)
    return dic

def verificar_tamanho_especiais(lista, opcao):
    for i in lista:
        if i == int(opcao[2]):
            return True
