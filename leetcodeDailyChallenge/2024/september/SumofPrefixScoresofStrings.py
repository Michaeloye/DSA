# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixMap = {}
        ans = [0] * len(words)
        
        for s in words:
            for i in range(len(s)):
                pre = s[:i + 1] 
                prefixMap[pre] = 1 + prefixMap.get(pre, 0)

        for i in range(len(words)):
            s = words[i]
            prefixCount = 0
            for j in range(len(words[i])):
                pre = s[:j + 1]
                if pre in prefixMap:
                    prefixCount += prefixMap[pre]
            ans[i] = prefixCount

        return ans