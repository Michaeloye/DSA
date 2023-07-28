from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        slow = 0
        fast = 1
        length = len(nums)

        # let slow remain on the first iteration of a particular number
        # so if we arrive at                1 1 1 2
        # slow will be at                   /
        # while fast will continue running      /
        # when fast reaches a number different from slow
        # slow will change to fast (that's the first occurence of the next number)

        while fast < length:
            if nums[fast] == nums[slow]:
                nums[fast] = 1000

            else:

                slow = fast
            fast += 1

        if 1000 in nums:
            nums.sort(reverse=False)
            print(nums)
            return nums.count(1000)

        return len(nums)


soln = Solution()
nums = [1, 1, 2]
print(soln.removeDuplicates(nums))
