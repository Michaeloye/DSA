# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderHashMap = {0: -1}
        subSum = 0

        for i in range(len(nums)):
            subSum += nums[i]
            rem = subSum % k

            if not rem in remainderHashMap:
                remainderHashMap[rem] = i

            elif i - remainderHashMap[rem] >= 2:
                return True

        return False