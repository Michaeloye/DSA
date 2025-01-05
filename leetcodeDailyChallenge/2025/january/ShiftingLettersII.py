# https://leetcode.com/problems/shifting-letters-ii/description/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        MOD = 26
        s = [ord(c) - ord('a') for c in s]
        prefixDiff = [0] * (len(s) + 1)

        for l, r, d in shifts:
            if d == 0:
                prefixDiff[l] += 1
                prefixDiff[r + 1] -= 1
            elif d == 1:
                prefixDiff[l] -= 1
                prefixDiff[r + 1] += 1
        
        diff = 0
        for i in reversed(range(len(prefixDiff))):
            diff += prefixDiff[i]
            s[i - 1] += diff
            s[i - 1] = s[i - 1] % MOD
        
        s = [chr(n + ord('a')) for n in s]

        return "".join(s)
