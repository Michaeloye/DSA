# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l < r:
            left = s[l]
            right = s[r]

            if left == right:
                l += 1
                r -= 1
                while l <= r and s[l] == left:
                    l += 1
                while l <= r and s[r] == right:
                    r -= 1
            else:
                break
        
        return r - l + 1