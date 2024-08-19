# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        
        stack = []
        
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                subRes = 0

                if token == '+':
                    subRes = b + a
                if token == '-':
                    subRes = b - a
                if token == '*':
                    subRes = b * a
                if token == '/':
                    subRes = int(b / a)
                stack.append(subRes)
            else:
                stack.append(int(token))

        return stack[0]
