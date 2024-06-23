# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        m = 0
        oddCount = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                oddCount += 1
            
            while oddCount > k:
                if nums[l] % 2 == 1:
                    oddCount -= 1

                l += 1
                m = l
            if oddCount == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += m - l + 1

        return res