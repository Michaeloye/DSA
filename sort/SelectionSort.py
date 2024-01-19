def selectionSort(array):

    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array) - 1):
            if array[j] < array[min]:
                min = j

        tmp = array[i]
        array[i] = array[min]
        array[min] = tmp

    return array


print(selectionSort([1, 5, 7, 9, 2, 4, 6, 9, 3]))
