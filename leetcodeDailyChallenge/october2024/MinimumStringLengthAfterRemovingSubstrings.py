# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# O(n^2) solution
class Solution:
    def minLength(self, s: str) -> int:

        while True:
            if "AB" in s:
                s = s.replace("AB", "")
            elif "CD" in s:
                s = s.replace("CD", "")
            else:
                break
        return len(s)

# O(n) solution
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for letter in s:
            stack.append(letter)

            if len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B") or
                (stack[-2] == "C" and stack[-1] == "D")
            ):
                stack.pop()
                stack.pop()
        
        return len(stack)