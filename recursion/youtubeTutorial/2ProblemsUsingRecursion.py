# print name N times using Recursion

# i -> iteration
# n -> number of times
def printName(i, n):
    if i > n:
        return
    print("MIKE")

    printName(i + 1, n)


printName(1, 5)
