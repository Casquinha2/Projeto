import json

def escrever_ficheiro_json(nome_ficheiro, j,g,jj):
    
    tudo = [j, g, jj]

    json_string = json.dumps(tudo)
    json_file = open(nome_ficheiro, "x")

    json_file.write(json_string)
    json_file.close()

def escrever_ficheiro_json_sgrelha(nome_ficheiro, j):
    nada =[]
    tudo = [j, nada]

    json_string = json.dumps(tudo)
    json_file = open(nome_ficheiro, "x")

    json_file.write(json_string)
    json_file.close()


def ler_ficheiro_json(nome_ficheiro):
    with open(nome_ficheiro) as f:
        data = json.load(f)
    return data

def ler_ficheiro_json_sgrelha(nome_ficheiro):
    with open(nome_ficheiro) as f:
        data = json.load(f)
    return data