# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        # change every negative num in arr to lenghth of the array + 1
        for i in range(length):
            if i <= 0:
                nums[i] = length + 1

        for i in range(length):
            curr = abs(nums[i]) - 1

            if curr >= length:
                continue

            # change nums[curr] as negative to num to show that it has been seen
            if nums[curr] > 0:
                nums[curr] = -1 * nums[curr]

        for i in range(length):
            if nums[i] >= 0:
                return i + 1

        return length + 1
