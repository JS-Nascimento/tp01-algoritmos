def soma_lista(lista):

    if not lista:
        return 0

    return lista[0] + soma_lista(lista[1:])

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 8, 9, 15, 35, 28]
    resultado = soma_lista(numeros)
    print(f"A soma dos elementos {numeros} é: {resultado}")
