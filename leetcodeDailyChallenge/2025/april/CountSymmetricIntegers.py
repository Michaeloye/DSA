# https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for n in range(low, high + 1):
            n = list(str(n))
            if len(n) % 2 == 1:
                continue

            mid = len(n) // 2
            left = [int(x) for x in n[:mid]]
            right = [int(x) for x in n[mid:]]

            if sum(left) == sum(right):
                ans += 1
        return ans