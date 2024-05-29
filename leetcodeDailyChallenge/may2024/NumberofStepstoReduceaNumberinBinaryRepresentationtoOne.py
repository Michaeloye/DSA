# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        ans = 0

        while num != 1:
            ans += 1
            if num % 2 == 1:
                num += 1
                continue
            if num % 2 == 0:
                num = num // 2

        return ans

# solve without changing to decimal
class Solution:
    def numSteps(self, s: str) -> int:

        def addOne(s):
            s = list(s)
            i = len(s) - 1

            while i >= 0 and s[i] == "1":
                s[i] = "0"
                i -= 1

            if i == -1:
                s = ["1"] + s
            else:
                s[i] = "1"
            return "".join(s)
        res = 0
        while s != "1":
            res += 1

            if s[-1] == "0":
                s = s[:-1]
            else:
                s = addOne(s)

        return res