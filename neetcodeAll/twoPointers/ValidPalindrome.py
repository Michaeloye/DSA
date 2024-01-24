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
