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


# add another solution
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)
        
        for n1, n2 in zip(target, arr):
            count[n1] += 1
            count[n2] -= 1

        for n in count:
            if count[n] != 0:
                return False
        return True