# https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        minNum = min(nums)
        maxNum = max(nums)
        ans = maxNum

        l = minNum
        r = maxNum

        def checkCapability(c):
            count = 0
            i = 0

            while i < len(nums):
                if nums[i] <= c:
                    i += 2
                    count += 1
                else:
                    i += 1
            return True if count >= k else False
        while l <= r:
            m = l + (r - l) // 2

            if checkCapability(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans