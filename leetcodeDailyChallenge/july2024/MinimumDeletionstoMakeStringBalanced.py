# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

class Solution:
    def minimumDeletions(self, s: str) -> int:
        aRightCount = 0

        for c in s:
            aRightCount += 1 if c == 'a' else 0

        bLeftCount = 0
        res = len(s)

        for c in s:
            if c == "a":
                aRightCount -= 1

            res = min(aRightCount + bLeftCount, res)

            if c == "b":
                bLeftCount += 1

        return res