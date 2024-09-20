# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s = list(s)
        def isPalindrome(s):
            return s == s[::-1]

        if isPalindrome(s):
            return "".join(s)

        left = []

        for i in range(len(s) - 1, 0, -1):
            left.append(s[i])
            formed = left + s

            if isPalindrome(formed):
                return "".join(formed)

