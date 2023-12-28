from typing import (
    List,
)


class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """

    def wiggle_sort(self, nums: List[int]):
        # write your code here
        # 3 5 2 1 6 4
        # 3 5 1 6 2 4
        for i in range(1, len(nums)):
            status = i % 2

            if status == 1:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                if nums[i] > nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

soln = Solution()
nums = [3, 1]

soln.wiggle_sort(nums)
print(nums)