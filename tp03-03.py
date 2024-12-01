def hanoi(n, origem, destino, auxiliar):
    """
    O problema da Torre de Hanói.

    :param n: Número de discos.
    :param origem: Pino de origem.
    :param destino: Pino de destino.
    :param auxiliar: Pino auxiliar.
    """
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return

    # Passo 1: Mova os n-1 discos para o auxiliar
    hanoi(n - 1, origem, auxiliar, destino)

    # Passo 2: Mova o disco maior para o destino
    print(f"Mova o disco {n} de {origem} para {destino}")

    # Passo 3: Mova os n-1 discos do auxiliar para o destino
    hanoi(n - 1, auxiliar, destino, origem)

# Exemplo de uso
if __name__ == "__main__":
    n = int(input("Digite o número de discos: "))
    hanoi(n, "Origem", "Destino", "Auxiliar")
