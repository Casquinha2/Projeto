def adicionar_jogador(nome):
    dicionario = {"jogador": nome, "jogos": 0, "Pontos": 0}
    return dicionario

def remover_jogador(nome, lista):
    for i in lista:
        jogador = i.get("jogador")
        if jogador == nome:
            lista.remove(i)
            return lista
