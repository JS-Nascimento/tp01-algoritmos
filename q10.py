def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

listas_de_strings = [
    ["banana", "maçã", "manga", "cereja", "laranja"],
    ["zebra", "elefante", "cachorro", "gato", "urso"],
    ["dispositivo", "algoritmo", "função", "variável", "constante"],
    ["a", "ab", "abc"],
    ["python", "Python", "python3", "Python2"],
    []
]

for lista in listas_de_strings:
    print("Lista original:", lista)
    bubble_sort_strings(lista)
    print("Lista ordenada:", lista)
    print("-" * 30)
