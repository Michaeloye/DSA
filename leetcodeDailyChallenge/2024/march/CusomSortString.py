# https://leetcode.com/problems/custom-sort-string/description/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sCount = {}
        ans = ''

        for letter in s:
            sCount[letter] = 1 + sCount.get(letter, 0)

        for letter in order:
            if letter in sCount:
                ans += letter * sCount[letter]
                sCount.pop(letter)

        for rem in sCount:
            ans += rem * sCount[rem]

        return ans