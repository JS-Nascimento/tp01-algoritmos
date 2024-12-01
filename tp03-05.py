def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]  # Menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Maiores que o pivô

    return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    array = [8, 3, 1, 7, 0, 10, 2]
    print("Array original:", array)
    sorted_array = quicksort(array)
    print("Array ordenado:", sorted_array)
