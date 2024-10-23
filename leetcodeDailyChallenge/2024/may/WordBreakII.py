# https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def dfs(i):
            if i == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w in wordDict:
                    cur.append(w)
                    dfs(j + 1)
                    cur.pop()
        
        cur = []
        res = []
        dfs(0)
        return res
