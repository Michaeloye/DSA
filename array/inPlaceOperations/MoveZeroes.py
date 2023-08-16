from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1
        length = len(nums)
        
        while slow < length:
          if(nums[slow] == 0) and fast < length:
            while nums[fast] == 0:
              if(fast== length - 1):
                return nums
              fast += 1
            nums[slow] = nums[fast]
            nums[fast] = 0
          slow += 1
          fast += 1

        return nums

soln = Solution()

nums = [0,0,0]
print(soln.moveZeroes(nums))