# https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        setNums = set(nums)
        uniqueNums = set()
        ans = [1, 0]

        for i in range(n):
            val = nums[i]
            # check for duplicate number
            if val in uniqueNums:
                ans[0] = val

            # check for missing number
            if val + 1 <= n and val + 1 not in setNums:
                ans[1] = val + 1
            elif val - 1 > 0 and val - 1 not in setNums:
                ans[1] = val - 1
            uniqueNums.add(val)

        return ans
