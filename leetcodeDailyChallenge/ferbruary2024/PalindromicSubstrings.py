# https://leetcode.com/problems/palindromic-substrings/

# O(n^3)
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

# optimized O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)

        # for odd length palindromes
        for i in range(len(s)):
            if i > 0 and i < len(s):
                l = i - 1
                r = i + 1

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
            
        # for even length palindromes
        for i in range(len(s) ):
            l = i
            r = l + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans

# well structured
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)

        for i in range(len(s)):
            # for odd length palindromes
            ans += self.countPali(s, i - 1, i + 1)

            # for even length palindromes
            ans += self.countPali(s, i, i + 1)
        
        return ans
        
    def countPali(self, s, l, r):
        res = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res

