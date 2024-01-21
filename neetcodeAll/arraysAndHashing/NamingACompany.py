# https://leetcode.com/problems/naming-a-company/

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        pair = set()
        firstLetterMap = {}
        distinctCount = 0

        for idea in ideas:
            if idea[0] in firstLetterMap:
                firstLetterMap[idea[0]].add(idea[1:])
            else:
                firstLetterMap[idea[0]] = set()
                firstLetterMap[idea[0]].add(idea[1:])

        for keyA in firstLetterMap:
            for keyB in firstLetterMap:
                if keyA == keyB:
                    continue

                if (keyA, keyB) in pair:
                    continue

                sameSuffixCount = 0
                for suffix in firstLetterMap[keyA]:
                    if suffix in firstLetterMap[keyB]:
                        sameSuffixCount += 1

                pair.add((keyA, keyB))
                pair.add((keyB, keyA))

                distinctA = len(firstLetterMap[keyA]) - sameSuffixCount
                distinctB = len(firstLetterMap[keyB]) - sameSuffixCount
                distinctCount += 2 * distinctA * distinctB

        return distinctCount
