class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 == 1:
            return False

        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            else:
                if stack and ((p == ')' and stack[-1] == '(') or (p == ']' and stack[-1] == '[') or (p == '}' and stack[-1] == '{')):
                    stack.pop()
                else:
                    return False

        return not bool(stack)