# https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        remMap = {0: 1}
        prefixSum = 0

        for n in nums:
            prefixSum += n
            rem = prefixSum % k

            if rem in remMap:
                res += remMap[rem]
                remMap[rem] += 1

            else:
                remMap[rem] = 1
        
        return res