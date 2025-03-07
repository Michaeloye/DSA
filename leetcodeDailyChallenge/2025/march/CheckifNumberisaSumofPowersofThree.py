# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        def backtrack(i, cur):
            if cur == n:
                return True
            if cur > n or 3 ** i > n:
                return False

            # pick
            if backtrack(i + 1, cur + 3 ** i):
                return True
            return backtrack(i + 1, cur)

        return backtrack(0, 0)

# optimal solution
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0

        while 3 ** i <= n:
            i += 1
        
        i -= 1

        while i >= 0:
            if 3 ** i > n:
                i -= 1
                continue
            
            n -= 3 ** i
            i -= 1

        return True if n == 0 else False