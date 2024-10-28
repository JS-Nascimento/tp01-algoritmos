def greatestUniqueNumber(array):

    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_unique = None

    for num, count in counts.items():
        if count == 1:
            if max_unique is None or num > max_unique:
                max_unique = num

    return max_unique

array = [5, 3, 9, 1, 9, 5, 7, 9, 3]
print(greatestUniqueNumber(array))
