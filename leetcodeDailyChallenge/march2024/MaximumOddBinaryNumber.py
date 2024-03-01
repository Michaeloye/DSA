# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0

        for el in s:
            if el == '1':
                count += 1

        return (count - 1) * "1" + (len(s) - count) * "0" + "1" 
