# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/?envType=daily-question&envId=2025-09-07

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # if n is even
        # iterate from 1 to n // 2, so 4 will go from 1 to 2
        # append numbers witn their negatie numbers too

        # if n is odd
        # iterate from 0 to n // 2, so 5 will go from 0 to 2
        # append numbers other than 0 with their negative numbers too

        ans = []

        if n % 2 == 0:
            for i in range(1, (n // 2) + 1):
                ans = ans + [-1 * i, i]
        else:
            for i in range(0, (n // 2) + 1):
                if i == 0:
                    ans = ans + [0]
                else:
                    ans = ans + [-1 * i, i]
        return ans
