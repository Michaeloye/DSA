# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            cur = 0
            for num in nums:
                cur += 1 if num >= i else 0
            if cur == i:
                return i

        return -1


# O(n logn) solution
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        prev = -1
        totalRight = len(nums)

        while i < len(nums):
            if nums[i] == totalRight or (prev < totalRight < nums[i]):
                return totalRight

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            prev = nums[i]
            i += 1
            totalRight = len(nums) - i

        return -1

# O(n) solution
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)

        for n in nums:
            index = min(n, len(nums))
            count[index] += 1
        
        totalRight = 0

        for i in range(len(nums), -1, -1):
            totalRight += count[i]
            if totalRight == i:
                return totalRight

        return -1
