# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                
                if words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans