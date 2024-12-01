def soma_recursiva(lista):

    if not lista:
        return 0

    return lista[0] + soma_recursiva(lista[1:])

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    print("A soma dos elementos é:", soma_recursiva(lista))
