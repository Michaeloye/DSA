# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 2
        if len(s) < 3:
            return s

        ans = s[:2]

        while i < len(s):
            if s[i] == s[i - 1] == s[i - 2]:
                i += 1
                continue
            ans += s[i]
            i += 1
        return ans