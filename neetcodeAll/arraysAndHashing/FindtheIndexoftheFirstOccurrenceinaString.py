# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if needle == "": return 0

    lps = [0] * len(needle)

    prevLPS = 0
    i = 0

    while i < len(needle):
      if needle[i] == needle[prevLPS]:
        lps[i] = lps[prevLPS] + 1
        i += 1
        prevLPS += 1
      elif prevLPS == 0:
        lps[i] = 0
        i += 1
      else:
        prevLPS = lps[prevLPS - 1]

    i = 0
    j = 0
    while i < len(haystack):
      if haystack[i] == needle[j]:
        i, j = i + 1, j + 1
      else:
        if j == 0:
          i += 1
        else:
          j = lps[j - 1]
      if j == len(needle):
        return i - len(needle)

    return -1
