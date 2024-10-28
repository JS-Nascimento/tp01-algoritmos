import random

primeira_mao = list(range(1, 14))
random.shuffle(primeira_mao)

segunda_mao = None
pilha_ordenada = []

while primeira_mao:
    segunda_mao = primeira_mao.pop(0)

    if not pilha_ordenada:
        pilha_ordenada.append(segunda_mao)
    else:
        inserido = False
        for i, carta in enumerate(pilha_ordenada):
            if segunda_mao < carta:
                pilha_ordenada.insert(i, segunda_mao)
                inserido = True
                break
        if not inserido:
            pilha_ordenada.append(segunda_mao)

    segunda_mao = None

print("Pilha de cartas ordenada:", pilha_ordenada)

