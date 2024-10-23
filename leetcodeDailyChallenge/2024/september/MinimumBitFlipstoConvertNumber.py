# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def decToBin(num):
            binary = []
            dec = num

            while dec:
                rem = dec % 2
                binary.append(str(rem))
                dec = dec // 2
            return binary[::-1]

        ans = 0
        diff = start ^ goal
        binDiff = decToBin(diff)

        for c in binDiff:
            if c == "1":
                ans += 1
        
        return ans