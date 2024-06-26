# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        total = 0

        for i in range(k):
            if s[i] in vowels:
                total += 1
        res = total
        for r in range(k, len(s)):
            if s[r] in vowels:
                total += 1

            if s[l] in vowels:
                total -= 1

            l += 1
            res = max(res, total)

        return res