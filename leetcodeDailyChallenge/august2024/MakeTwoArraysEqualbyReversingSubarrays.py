# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetCount = {}
        arrCount = {}
        if len(target) != len(arr):
            return False

        for a, b in zip(target, arr):
            targetCount[a] = 1 + targetCount.get(a, 0)
            arrCount[b] = 1 + arrCount.get(b, 0)

        return targetCount == arrCount