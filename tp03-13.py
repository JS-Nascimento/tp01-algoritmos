def is_palindrome_recursivo(palavra):

    if len(palavra) <= 1:
        return True

    if palavra[0] != palavra[-1]:
        return False

    return is_palindrome_recursivo(palavra[1:-1])

if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    if is_palindrome_recursivo(palavra):
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' não é um palíndromo!")
