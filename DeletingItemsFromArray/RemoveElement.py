from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        c = nums.count(val)
        i = 0
        j = len(nums) - 1

        while i < j:
            print(c)
            if nums[i] == val:
                while nums[j] == val and j > i:
                    j -= 1

                nums[i], nums[j] = nums[j], nums[i]
                j -= 1

            i += 1
            print(nums)

        return len(nums) - c


soln = Solution()
nums = [0, 0]
val = 0
end = soln.removeElement(nums, val)
print(nums[:end])

# MORE EFFICIENT


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in nums:
            if fast != val:

                nums[slow] = fast
                slow += 1

        return slow
