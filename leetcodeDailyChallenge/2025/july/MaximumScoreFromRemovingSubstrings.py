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
