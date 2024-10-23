# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        subArrSums = [] 
        
        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum = (curSum + nums[j]) % MOD
                subArrSums.append(curSum)
        
        subArrSums.sort()
        ans = 0

        for i in range(left - 1, right):
            ans = (ans + subArrSums[i]) % MOD
        return ans
