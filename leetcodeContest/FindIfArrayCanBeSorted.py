# https://leetcode.com/contest/biweekly-contest-122/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countSetBits(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count

        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):

                if countSetBits(nums[j]) == countSetBits(nums[j + 1]) and nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if (swapped == False):
                break

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                return False

        return True
