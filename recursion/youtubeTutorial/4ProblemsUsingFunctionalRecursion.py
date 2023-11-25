

array = [1, 2, 3, 4, 5]


def reverseArray1(l, r):
    if l >= r:
        return

    array[l], array[r] = array[r], array[l]

    reverseArray1(l + 1, r - 1)


reverseArray1(0, len(array) - 1)


def reverseArray2(i):
    n = len(array)
    if i >= n//2:
        return

    array[i], array[n - i - 1] = array[n - i - 1], array[i]
    reverseArray2(i + 1)


reverseArray2(0)

word = "MADAM"


def isPalindrome(i):
    n = len(word)
    if i >= n / 2:
        return True
    if word[i] != word[n - i - 1]:
        return False

    return isPalindrome(i + 1)


isPalindrome(0)
