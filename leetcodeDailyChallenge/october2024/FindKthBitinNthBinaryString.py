# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertBin(num):
            inverted = ""
            for b in num:
                inverted += "1" if b == "0" else "0"
            return inverted

        binary = "0"
        while n > 1:
            inverted = invertBin(binary)
            rightSide = inverted[::-1]
            binary += "1"
            binary += rightSide
            n -= 1

        for i in range(len(binary)):
            if i == k - 1:
                return binary[i]
