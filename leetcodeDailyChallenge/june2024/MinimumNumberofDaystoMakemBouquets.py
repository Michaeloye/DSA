# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)

        if m * k > N:
            return -1
        
        def possible(num):
            adjacentCount = 0
            count = 0

            for day in bloomDay:
                if day <= num:
                    count += 1
                else:
                    adjacentCount += count // k
                    count = 0

            adjacentCount += count // k
            return adjacentCount >= m

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low