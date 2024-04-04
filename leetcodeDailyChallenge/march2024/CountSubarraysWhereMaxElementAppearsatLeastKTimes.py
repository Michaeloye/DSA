class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        maxNum = max(nums)
        count = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == maxNum:
                count += 1
            
            while count > k or (l <= r and count >= k and nums[l] != maxNum):

                if nums[l] == maxNum:
                    count -= 1
                l += 1
            if count == k:
                res += l + 1

        return res