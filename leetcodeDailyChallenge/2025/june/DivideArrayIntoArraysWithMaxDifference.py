# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        subAns = []

        for i in range(n):
            if i > 0 and i % 3 == 0:
                ans.append(subAns[:])
                subAns = []
            elif (i + 1) % 3 == 0 and nums[i] - nums[i - 2] > k:
                return []
            subAns.append(nums[i])
        ans.append(subAns[:])
        return ans

# OPTIMIZED SOLUTION
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i + 3])
        return ans
