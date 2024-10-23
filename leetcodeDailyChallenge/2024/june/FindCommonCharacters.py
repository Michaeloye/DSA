# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonMap = {}
        ans = []
        for letter in words[0]:
            commonMap[letter] = 1 + commonMap.get(letter, 0)

        for word in words[1:]:
            letterCount = {}
            for letter in word:
                letterCount[letter] = 1 + letterCount.get(letter, 0)
            for letter in commonMap:
                commonMap[letter] = min(commonMap[letter], letterCount.get(letter, 0))

        for letter in commonMap:
            for i in range(commonMap[letter]):
                ans.append(letter)

        return ans
