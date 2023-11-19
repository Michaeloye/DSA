# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
