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


# using two pointer method
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        l, r = 0, n - 1

        while n != len(ans):
            ans.append(nums[l])
            l += 1

            if l <= r:
                ans.append(nums[r])
                r -= 1
        return ans