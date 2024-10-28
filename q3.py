def busca_linear(array, alvo):
    passos = 0
    for index, valor in enumerate(array):
        passos += 1
        if valor == alvo:
            return (True, passos)
    return (False, passos)

array = [2, 4, 6, 8, 10, 12, 13]

alvo = 8

encontrado, passos = busca_linear(array, alvo)

if encontrado:
    print(f"O número {alvo} foi encontrado em {passos} passos.")
else:
    print(f"O número {alvo} não foi encontrado. Busca levou {passos} passos.")
