# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def stringToInt(s):
            num = []
            for c in s:
                stringNum = str(ord(c) - ord('a') + 1)
                num.append(stringNum)

            return "".join(num)
        
        num = stringToInt(s)
        
        while k:
            acc = 0
            for n in num:
                acc += int(n)
            num = str(acc)
            k -= 1
        return int(num)
