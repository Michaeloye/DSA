# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        letters = set(s)
        ans = 0

        for letter in letters:
            l = s.index(letter)
            r = s.rindex(letter)

            between = len(set(s[l+1:r]))
            ans += between

        return ans