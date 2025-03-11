# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
      stringCount = {}
      l = 0
      ans = 0

      for r in range(len(s)):
        stringCount[s[r]] = 1 + stringCount.get(s[r], 0)

        while len(stringCount) == 3:
          ans += len(s) - r
          stringCount[s[l]] -= 1
          if stringCount[s[l]] == 0:
            stringCount.pop(s[l])
          l += 1
      return ans
