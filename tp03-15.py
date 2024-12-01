def contar_repeticoes(string, caractere):

    if not string:
        return 0
    return (1 if string[0] == caractere else 0) + contar_repeticoes(string[1:], caractere)

if __name__ == "__main__":
    string = "araraquarense"
    caractere = "a"
    resultado = contar_repeticoes(string, caractere)
    print(f"O caractere '{caractere}' aparece {resultado} vezes na string '{string}'.")
