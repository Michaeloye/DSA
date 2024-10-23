# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        strCount = {}

        for s in arr:
            strCount[s] = 1 + strCount.get(s, 0)
        
        distinct = 0
        for s in strCount:
            if strCount[s] == 1:
                distinct += 1
            if distinct == k:
                return s
        return ""
