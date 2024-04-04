# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        maxRes = 0
        res = 0

        for char in s:
            if char == "(":
                res += 1
            elif char == ")":
                maxRes = max(maxRes, res)
                res -= 1

        return maxRes
