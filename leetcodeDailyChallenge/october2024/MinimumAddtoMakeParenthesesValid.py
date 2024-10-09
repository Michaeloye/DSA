# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and stack[-1] == "(" and c == ")":
                stack.pop()
            else:
                stack.append(c)
                
        return len(stack)


# O(1) space complexity
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        extraOpen = 0
        extraClose = 0

        for c in s:
            if c == "(":
                extraOpen += 1
            else:
                extraOpen -= 1
                if extraOpen < 0:
                    extraClose += 1
                    extraOpen = 0
        
        return extraOpen + extraClose