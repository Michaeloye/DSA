# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans