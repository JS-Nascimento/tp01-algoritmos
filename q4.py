def busca_binaria(array, alvo):
    esquerda, direita = 0, len(array) - 1
    passos = 0
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        if array[meio] == alvo:
            return (True, passos)
        elif array[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return (False, passos)

array = [2, 4, 6, 8, 10, 12, 13]

alvo = 8
encontrado, passos = busca_binaria(array, alvo)

if encontrado:
    print(f"O número {alvo} foi encontrado em {passos} passo(s).")
else:
    print(f"O número {alvo} não foi encontrado. Busca levou {passos} passo(s).")
