# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrSet = set(arr)
        zeroCount = arr.count(0)

        for num in arrSet:
            if num == 0 and zeroCount > 1 and 2 * num in arrSet:
                return True
            elif num and 2 * num in arrSet:
                return True
        return False