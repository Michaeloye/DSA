# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        maxContiguousClose = 0
        for brack in s:
            if brack == ']':
                stack += 1
                maxContiguousClose = max(stack, maxContiguousClose)
            else:
                stack -= 1

        return (maxContiguousClose + 1) // 2
