# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numsMap = {}

        for num in arr:
            numsMap[num] = 1 + numsMap.get(num, 0)

        occurences = numsMap.values()
        uniqueOccurences = set(occurences)

        return len(occurences) == len(uniqueOccurences)
