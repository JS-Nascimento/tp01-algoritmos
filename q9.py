def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

listas_de_teste = [
    [64, 34, 25, 12, 22, 11, 90],
    [1, 2, 3, 4, 5],
    [5, 1, 4, 2, 8],
    [],
    [2],
    [99, 55, 4, 66, 28, 31, 19]
]

for lista in listas_de_teste:
    print("Lista original:", lista)
    bubble_sort(lista)
    print("Lista ordenada:", lista)
    print("-" * 30)
