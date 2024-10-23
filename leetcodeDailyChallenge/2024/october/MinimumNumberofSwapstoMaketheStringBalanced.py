# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        close = 0
        maxClose = 0

        for c in s:
            if c == "[":
                close -= 1
            elif c == "]":
                close += 1
                maxClose = max(maxClose, close)
        
        # on swapping once gets rid of two closing parentheses
        # ]]][[[
        return (maxClose +  1) // 2