# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # phase 1
        # remove subStr1
        ans = 0
        
        subStr1 =  "ab" if x > y else "ba"
        stack1 = []
        for c in s:
            if stack1 and stack1[-1] + c == subStr1:
                ans += max(x, y)
                stack1.pop()
            else:
                stack1.append(c)

        # phase 2
        # remove subStr2
        subStr2 = "ab" if x <= y else "ba"
        stack2 = []
        remS = "".join(stack1)

        for c in remS:
            if stack2 and stack2[-1] + c == subStr2:
                ans += min(x, y)
                stack2.pop()
            else:
                stack2.append(c)

        return ans

# OPTIMIZED CODE
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(pair, delta):
            stack = []
            ans = 0
            nonlocal s

            for c in s:
                if stack and stack[-1] + c == pair:
                    ans += delta
                    stack.pop()
                else:
                    stack.append(c)
            s = "".join(stack)
            return ans
        
        ans = 0
        pair = "ab" if x > y else "ba"
        ans += remove_pairs(pair, max(x, y))
        ans += remove_pairs(pair[::-1], min(x, y))
        
        return ans
