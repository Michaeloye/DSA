# https://leetcode.com/problems/group-anagrams

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = {}  # val: index
        anagramGroup = []
        nextIdx = 0

        for val in strs:
            wordSep = sorted(val)
            wordJoint = ''.join(wordSep)

            if wordJoint in strsMap:
                anagramGroup[strsMap[wordJoint]].append(val)
            else:
                strsMap[wordJoint] = nextIdx
                nextIdx += 1
                anagramGroup.append([val])

        return anagramGroup


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for l in s:
                pos = ord(l) - ord("a")
                count[pos] = 1

            res[tuple(count)].append(s)

        return res.values()
