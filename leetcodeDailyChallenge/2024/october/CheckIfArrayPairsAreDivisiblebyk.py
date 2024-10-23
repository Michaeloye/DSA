# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainderMap = {}

        for num in arr:
            rem = num % k
            remainderMap[rem] = 1 + remainderMap.get(rem, 0)
        
        if 0 in remainderMap:
            if remainderMap[0] % 2 == 1:
                return False

            remainderMap.pop(0)

        for rem in remainderMap:
            remMir = k - rem
            if remMir in remainderMap:
                if remainderMap[remMir] != remainderMap[rem]:
                    return False
            else:
                return False
        return True