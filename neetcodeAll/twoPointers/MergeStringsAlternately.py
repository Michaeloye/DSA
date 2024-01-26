# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j = 0
        ans = ""

        # combine word1 and word2
        for i in range(len(word1)):
            ans += word1[i]

            if j < len(word2):
                ans += word2[j]
                j += 1

        # check if there is any remainders in word2
        if j != len(word2):
            ans += word2[j:]

        return ans
