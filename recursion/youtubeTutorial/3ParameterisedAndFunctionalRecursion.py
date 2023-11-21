# calculating the sum of numbers up to the nth term

# parameterise
def nthSumP(i, n):
    if i < 1:
        print(n)
        return

    nthSumP(i-1, n + i)


nthSumP(3, 0)

# Functional


def nthSumF(n):
    if n == 0:
        return 0

    return n + nthSumF(n - 1)


print(nthSumF(3))


def nFactorial(n):
    if n == 1:
        return 1

    return n * nFactorial(n - 1)


print(nFactorial(3))
