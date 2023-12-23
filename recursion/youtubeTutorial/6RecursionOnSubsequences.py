
mainArray = [3, 1, 2]


def subsequence(index, arr):
    if index >= len(mainArray):
        print(arr)
        return

    arr.append(mainArray[index])
    subsequence(index + 1, arr)

    arr.pop()
    subsequence(index + 1, arr)


subsequence(0, [])
