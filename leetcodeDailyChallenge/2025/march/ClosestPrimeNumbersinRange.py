# https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        primeNums = []

        for num in range(left, right + 1):
            if isPrime(num):
                primeNums.append(num)

        ans = [-1, -1]
        minDiff = float('inf')

        for i in range(1, len(primeNums)):
            num1 = primeNums[i - 1]
            num2 = primeNums[i]
            diff = num2 - num1
            if diff < minDiff:
                ans = [num1, num2]
                minDiff = diff
            
        return ans


# Better solution
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        prevPrime = -1
        ans = [-1, -1]
        minDiff = float('inf')

        for num in range(left, right + 1):
            if isPrime(num):
                if prevPrime > 0:
                    diff = num - prevPrime
                    if diff < minDiff:
                        ans = [prevPrime, num]
                        minDiff = diff
                prevPrime = num

        return ans

# O(Nloglogn) time solution
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def generatePrimes():
            arr = [False, False] + [True] * (right - 1)

            for i in range(2, int(right ** 0.5) + 1):
                j = 2
                while i * j <= right:
                    arr[i * j] = False
                    j += 1
            
            primes = []
            for i in range(left, right + 1):
                if arr[i]:
                    primes.append(i)
            return primes

        primeNums = generatePrimes()
        print(primeNums)
        ans = [-1, -1]
        minDiff = right - left + 1

        for i in range(1, len(primeNums)):
            num1 = primeNums[i - 1]
            num2 = primeNums[i]
            diff = num2 - num1
            if diff < minDiff:
                ans = [num1, num2]
                minDiff = diff
            
        return ans
