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
        lista.append(0)
    for j in range(h):
        grelha.append(lista)
    return grelha


