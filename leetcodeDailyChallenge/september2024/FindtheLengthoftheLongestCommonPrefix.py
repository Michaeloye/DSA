# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        prefixNum = set()

        for n in arr1:
            while n and n not in prefixNum:
                prefixNum.add(n)
                n = n // 10
        
        ans = 0
        for n in arr2:
            while n and n not in prefixNum:
                n = n // 10

            if n:
                ans = max(ans, len(str(n)))
        return ans