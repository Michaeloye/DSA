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

# bitwise solution
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bitwise = 0

        for c in allowed:
            bit = 1 << (ord(c) - ord('a'))
            bitwise = bitwise | bit

        ans = len(words)
        for word in words:
            for c in word:
                bit = 1 << (ord(c) - ord('a'))
                if bit & bitwise == 0:
                    ans -= 1
                    break

        return ans