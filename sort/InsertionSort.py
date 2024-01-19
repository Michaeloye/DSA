def insertionSort(array):
    for i in range(1, len(array)):
        tmp = array[i]

        j = i - 1
        while j >= 0 and array[j] > tmp:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = tmp

    return array


print(insertionSort([1, 5, 7, 9, 2, 4, 6, 9, 3]))
