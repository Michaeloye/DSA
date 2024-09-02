# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        count = 0
        ans = 0
        
        l = 0

        for r in range(len(nums)):
            if nums[r] == maxNum:
                count += 1

            while count > k or (l <= r and count == k and nums[l] != maxNum):
                if nums[l] == maxNum:
                    count -= 1

                l += 1
            
            if count == k:
                ans += l + 1

        return ans