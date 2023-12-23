
mainArray = [3, 1, 2]

# T.C O(2^n)  S.C O(n), where n is lenght of the array


def subsequence(index, arr):
    if index >= len(mainArray):
        print(arr)
        return

    arr.append(mainArray[index])
    subsequence(index + 1, arr)

    arr.pop()
    subsequence(index + 1, arr)


subsequence(0, [])
