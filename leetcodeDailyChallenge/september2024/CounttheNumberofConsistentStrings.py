# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed = set(allowed)
        ans = 0

        for word in words:
            notAllowed = False
            for c in word:
                if c not in allowed:
                    notAllowed = True
                    break
            if not notAllowed:
                ans += 1
        
        return ans