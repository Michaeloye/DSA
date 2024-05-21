# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort(reverse=True)
        ans  = [0] * n

        for i in range(0, n, 2):
            ans[i] = nums.pop()

        for i in range(1, n, 2):
            ans[i] = nums.pop()

        return ans
