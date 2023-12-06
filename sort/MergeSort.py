def mergeSort(array):
    if len(array) <= 1:
        return

    mid = len(array) // 2
    leftPart = array[0: mid]
    rightPart = array[mid: len(array)]

    mergeSort(leftPart)
    mergeSort(rightPart)
    merge(leftPart, rightPart, array)


def merge(leftArray, rightArray, array):

    leftSize = len(leftArray)
    rightSize = len(rightArray)

    i, l, r = 0, 0, 0

    while (l < leftSize and r < rightSize):
        if (leftArray[l] <= rightArray[r]):
            array[i] = leftArray[l]
            l += 1
        else:
            array[i] = rightArray[r]
            r += 1

        i += 1

    while l < leftSize:
        array[i] = leftArray[l]
        l += 1
        i += 1

    while r < rightSize:
        array[i] = rightArray[r]
        r += 1
        i += 1


arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
mergeSort(arr)
print(arr)
