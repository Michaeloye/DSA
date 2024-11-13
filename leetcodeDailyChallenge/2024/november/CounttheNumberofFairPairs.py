# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binSearch(l, r, target):
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r

        ans = 0
        nums.sort()

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]

            ans += (
                binSearch(i + 1, len(nums) - 1, up + 1) - 
                binSearch(i + 1, len(nums) - 1, low)
            )
        return ans