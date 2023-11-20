# print name N times using Recursion

# i -> iteration
# n -> number of times
def printName(i, n):
    if i > n:
        return
    print("MIKE")

    printName(i + 1, n)


printName(1, 5)


# print linearly from 1 to N
# i -> iteration
# n -> number to print to
def printLinearly(i, n):
    if i > n:
        return

    print(i)
    printLinearly(i + 1, n)


printLinearly(0, 5)
