# https://leetcode.com/problems/maximum-odd-binary-number/


# another solution
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        el = [c for c in s]
        l = 0

        for i in range(len(el)):
            if el[i] == "1":
                el[l], el[i] = el[i], el[l]
                l += 1

        el[l - 1], el[-1] = el[-1], el[l - 1]
        return "".join(el)


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0

        for el in s:
            if el == '1':
                count += 1

        return (count - 1) * "1" + (len(s) - count) * "0" + "1" 