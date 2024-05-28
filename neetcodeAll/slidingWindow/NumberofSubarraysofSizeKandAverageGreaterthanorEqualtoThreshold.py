# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefixSum = [0] * len(arr)
        curr = 0
        res = 0
        
        # compute prefix sums
        for i in range(len(arr)):
            curr += arr[i]
            prefixSum[i] = curr

        for i in range(len(arr) - k + 1):
            left = prefixSum[i - 1] if i > 0 else 0
            right = prefixSum[i + k - 1]
            diff = right - left
            
            if diff / k >= threshold:
                res += 1

        return res

# add another solution
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = sum(arr[:k - 1])
        res = 0
        
        for l in range(len(arr) - k + 1):
            curSum += arr[l + k - 1]

            if curSum / k >= threshold:
                res += 1
            
            curSum -= arr[l]
        return res

