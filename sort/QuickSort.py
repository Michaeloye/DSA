
def quickSort(array, start, end):
    if (end <= start):
        return

    print(array, start, end)
    pivot = array[end]

    i = start - 1

    for j in range(start, end + 1):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1

    array[i], array[end] = array[end], array[i]

    quickSort(array, start, i - 1)
    quickSort(array, i + 1, end)


arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]

quickSort(arr, 0, len(arr) - 1)
print(arr)
