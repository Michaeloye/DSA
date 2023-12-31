mainArr = [1, 2, 1]
targetSum = 3


def subsequence(index, array, sum):
    if index >= len(mainArr):
        if sum == targetSum:
            print(array)
        return

    array.append(mainArr[index])
    sum += mainArr[index]
    subsequence(index + 1, array, sum)

    array.pop()
    sum -= mainArr[index]

    subsequence(index + 1, array, sum)


# subsequence(0, [], 0)


# print only one subsequence
def oneSubsequence(index, array, sum):
    if index >= len(mainArr):
        # condition satisfied
        if sum == targetSum:
            print(array)
            return True

        # condition not satisfied
        return False

    array.append(mainArr[index])
    sum += mainArr[index]
    if oneSubsequence(index + 1, array, sum):
        return True

    array.pop()
    sum -= mainArr[index]

    if oneSubsequence(index + 1, array, sum):
        return True
    return False


# oneSubsequence(0, [], 0)


# count all
def countSubsequence(index, sum):
    if index >= len(mainArr):
        # condition satisfied
        if sum > targetSum:
            return 0
        if index == len(mainArr):
            if sum == targetSum:
                return 1

            # condition not satisfied
            return 0

    sum += mainArr[index]
    l = countSubsequence(index + 1, sum)

    sum -= mainArr[index]
    r = countSubsequence(index + 1, sum)
    return l + r


print(countSubsequence(0, 0))
