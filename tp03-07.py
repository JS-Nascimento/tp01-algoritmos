def quickselect(arr, k):

    if len(arr) == 1:
        return arr[0]

    pivot = arr[-1]

    left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
    right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
    count_pivot = arr.count(pivot)

    # Índice do pivô
    left_size = len(left)

    # Decisão
    if k < left_size:
        return quickselect(left, k)
    elif k < left_size + count_pivot:
        return pivot
    else:
        return quickselect(right, k - left_size - count_pivot)

if __name__ == "__main__":
    arr = [3, 2, 1, 5, 4]
    k = 3
    print(f"O {k + 1}-ésimo menor elemento é:", quickselect(arr, k))
