# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        ans = False

        while l <= r:
            if s[l] == s[r]:
                ans = True
            if s[l] != s[r]:
                # check withour r
                subStrL = s[l:r]
                withoutR = subStrL == subStrL[::-1]

                # check without l
                subStrR = s[l + 1: r + 1]
                withoutL = subStrR == subStrR[::-1]

                ans = withoutR or withoutL
                break

            l += 1
            r -= 1

        return ans
