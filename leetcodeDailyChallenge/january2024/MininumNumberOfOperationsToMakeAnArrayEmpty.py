# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty

# solution using dp
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def minOpForNum(n):
            dp = [float('inf')] * (n + 1)
            dp[0] = 0
            for i in range(1, n + 1):
                if i >= 3:
                    dp[i] = min(dp[i], dp[i - 3] + 1)
                if i >= 2:
                    dp[i] = min(dp[i], dp[i - 2] + 1)
            return dp[n]

        numsMap = {}
        total = len(nums)

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)

        noOfOperations = 0

        print(numsMap)
        for key in numsMap:
            val = numsMap[key]
            if val == 1:
                return -1
            if val % 3 == 0:
                noOfOperations += val // 3
                total -= val
            else:
                noOfOperations += minOpForNum(val)
                total -= val

        return noOfOperations if total == 0 else -1

# OPTIMAL SOLUTION


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans
