# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t in ops:
                a = stack.pop()
                b = stack.pop()
                subRes = 0

                if t == "+":
                    subRes = a + b
                elif t == "-":
                    subRes = b - a
                elif t == "*":
                    subRes = b * a
                elif t == "/":
                    subRes = int(b /a)
                stack.append(subRes)
            else:
                stack.append(int(t))
        
        return stack[0]