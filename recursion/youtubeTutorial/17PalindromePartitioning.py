# https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(string):
            l = 0
            r = len(string) - 1
            
            while l <= r:
                if string[l] != string[r]:
                    return False
                
                l += 1
                r -= 1
            return True

        ans = []
        ds = []

        def dfs(i):
            # base case
            if i == len(s):
                ans.append(ds[:])
                return
            for j in range(i, len(s)):
                if isPali(s[i:j + 1]):
                    ds.append(s[i:j + 1])
                    dfs(j + 1)
                    ds.pop()
        dfs(0)
        return ans


