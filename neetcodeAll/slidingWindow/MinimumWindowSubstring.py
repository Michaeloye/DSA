# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        windowMap = {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        ans = [-1, -1]
        ansLen = float("inf")
        l = 0

        need = len(tMap)
        have = 0

        for r in range(len(s)):
            c = s[r]

            if c in tMap:
                windowMap[c] = 1 + windowMap.get(c, 0)

                if windowMap[c] == tMap[c]:
                    have += 1
            
            while have == need:
                if r - l + 1 < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1
                
                if s[l] in tMap:
                    windowMap[s[l]] -= 1
                    if windowMap[s[l]] < tMap[s[l]]:
                        have -= 1

                l += 1
        r = ans[1]
        l = ans[0]

        return s[l:r + 1]