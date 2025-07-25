# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_list = list(nums_set)
        nums_list.sort(reverse=True)

        ans = nums_list[0]
        for n in nums_list[1:]:
            cur = ans + n
            if cur < ans:
                return ans

            ans += n
        return ans
