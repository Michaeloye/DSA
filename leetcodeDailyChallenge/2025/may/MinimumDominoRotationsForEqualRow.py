# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = tops[0]
        b = bottoms[0]

        for target in [t, b]:
            missingT = 0
            missingB = 0
            for i in range(len(tops)):
                top = tops[i]
                bottom = bottoms[i]
                if top != target and bottom != target:
                    break
                if top != target:
                    missingT += 1
                if bottom != target:
                    missingB += 1
                if i == len(tops) - 1:
                    return min(missingT, missingB)
        return -1