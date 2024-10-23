# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(word, i, j):
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res