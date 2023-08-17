from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        slow = 0
        fast = 1
        length = len(nums)

        while slow < length:
            if (nums[slow] % 2 != 0 and fast < length):
                while (nums[fast] % 2 != 0):
                    fast += 1
                    if (fast == length):
                        return nums
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
        return nums


soln = Solution()
nums = [3, 1, 2, 4]
print(soln.sortArrayByParity(nums))
