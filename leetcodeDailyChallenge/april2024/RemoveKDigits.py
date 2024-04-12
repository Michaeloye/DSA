# https://leetcode.com/problems/remove-k-digits

# Monotonic stack
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for a in num:
            while k > 0 and stack and a < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(a)
        stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip("0")

        return res if res else "0"