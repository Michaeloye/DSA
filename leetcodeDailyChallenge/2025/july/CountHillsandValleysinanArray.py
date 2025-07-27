# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        prev_num = nums[0]

        for i in range(1, len(nums) - 1):
            next_num = nums[i + 1]
            cur_num = nums[i]

            if cur_num > prev_num and cur_num > next_num:
                ans += 1
            elif cur_num < prev_num and cur_num < next_num:
                ans += 1

            if cur_num != next_num:
                prev_num = cur_num

        return ans
