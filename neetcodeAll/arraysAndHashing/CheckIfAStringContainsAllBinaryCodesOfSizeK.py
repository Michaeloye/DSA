# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        codeSet = set()

        for i in range(len(s) - k + 1):
            subStr = s[i:i + k]
            if subStr in codeSet:
                continue
            codeSet.add(subStr)
            if len(codeSet) == 2 ** k:
                return True
        return False
