# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

class Solution:

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numsMap = {}

        for i in nums:
            numsMap[i] = 1 + numsMap.get(i, 0)

        ans = [[] for i in range(max(numsMap.values()))]

        while nums:
            curr = nums.pop()
            idx = numsMap[curr] - 1
            ans[idx].append(curr)

            numsMap[curr] -= 1
        return ans
