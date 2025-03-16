# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        if total < k:
            return 0

        l = 1
        r = total // k
        ans = 0

        def checkPiles(n):
            count = 0

            for c in candies:
                if c // n:
                    count += c // n
            return True if count >= k else False

        while l <= r:
            m = l + (r - l) // 2

            if checkPiles(m):
                ans = max(ans, m)
                l = m + 1
            else:
                r = m - 1

        return ans
