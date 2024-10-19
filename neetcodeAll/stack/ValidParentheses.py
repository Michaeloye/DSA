# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openParen = ['(', '[', '{']
        closeMap = {')': '(', '}': '{', ']': '['}

        if len(s) % 2 == 1:
            return False

        for c in s:
            if c in openParen:
                stack.append(c)
            else:
                top = stack[-1] if stack else ""
                if closeMap[c] == top:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False