# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)

        for i in range(len(s) - 1):
            subStr = [s[i]]
            for j in range(i + 1,len(s)):
                subStr.append(s[j])
                if subStr == subStr[::-1]:
                    ans += 1
        
        return ans