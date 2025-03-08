# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            
            m = l + (r - l) // 2
            ans = min(ans, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return ans
