# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        totalOnesCount = nums.count(1)
        numberOfOnes = 0
        maxNumberOfOnes = 0

        l = 0
        for r in range(2 * N):
            if nums[r % N]:
                numberOfOnes += 1

            if r - l + 1 > totalOnesCount:
                numberOfOnes -= nums[l % N]
                l += 1

            maxNumberOfOnes = max(maxNumberOfOnes, numberOfOnes)
        return totalOnesCount - maxNumberOfOnes