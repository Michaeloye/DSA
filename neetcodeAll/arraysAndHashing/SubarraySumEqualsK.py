# https://leetcode.com/problems/subarray-sum-equals-k/

# BRUTE FORCE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numOfSubArrs = 0
        for idx, num in enumerate(nums):
            subSeqSum = 0
            for otherNum in nums[idx:]:
                subSeqSum += otherNum
                if subSeqSum == k:
                    numOfSubArrs += 1
        return numOfSubArrs


# OPTIMIZE SOLUTION
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numOfSubArrs = 0
        prefixSumMap = {0: 1}

        prefixSum = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in prefixSumMap:
                numOfSubArrs += prefixSumMap[prefixSum - k]

            prefixSumMap[prefixSum] = 1 + prefixSumMap.get(prefixSum, 0)

        return numOfSubArrs
