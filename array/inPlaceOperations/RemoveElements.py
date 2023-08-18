from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in nums:
            if fast != val:
                nums[slow] = fast
                slow += 1

        print(nums)
        return slow


soln = Solution()
nums = [0, 0, 1]
val = 0

print(soln.removeElement(nums, val))
