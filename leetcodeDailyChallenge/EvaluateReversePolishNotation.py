# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["*", "/", "-", "+"])
        
        for token in tokens:
            if token in ops:
                r = stack.pop()
                l = stack.pop()
                
                res = 0
                if token == "+":
                    res = l + r
                elif token == "-":
                    res = l - r
                elif token == "*":
                    res = l * r
                else:
                    res = int(l/r)
                stack.append(int(res))
            else:
                stack.append(int(token))
            
        return stack.pop()