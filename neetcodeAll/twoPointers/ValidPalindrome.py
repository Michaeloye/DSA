class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        lowerS = ""

        for char in s:
            tmp = char
            if ord(char) in range(ord('A'), ord('Z') + 1):
                diff = ord(char) - ord('A')
                lowerCaseChar = chr(ord('a') + diff)
                tmp = lowerCaseChar
            elif ord(char) in range(ord('0'), ord('9') + 1) or ord(char) in range(ord('a'), ord('z') + 1):
                lowerCaseChar = tmp
            else:
                continue
            lowerS += tmp

        return lowerS == lowerS[::-1]


# add another solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = s.lower()
        s = s.replace(" ", "")
        r = len(s) - 1

        if len(s) == 1:
            return True

        while l <= r:
            while l <= r and not (ord(s[l]) in range(ord('a'), ord('z') + 1) or ord(s[l]) in range(ord('0'), ord('9') + 1)):
                l += 1
            while l <= r and not (ord(s[r]) in range(ord('a'), ord('z') + 1) or ord(s[r]) in range(ord('0'), ord('9') + 1)):
                r -= 1

            if l <= r and s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True