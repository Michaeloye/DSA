# https://leetcode.com/problems/rotate-array/

# O(n) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)

        for i in range(len(nums)):
            idx = (i + k) % len(nums)
            res[idx] = nums[i]

# O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]

                l += 1
                r -= 1
        # [1,2,3,4,5]
        # reverse the whole array
        helper(0, len(nums) - 1)
        # [5,4,3,2,1]

        # reverse from 0 to k - 1
        helper(0, k - 1)
        # [4,5,3,2,1]

        # reverse from k to end
        helper(k, len(nums) - 1)
        # [4,5,1,2,3]