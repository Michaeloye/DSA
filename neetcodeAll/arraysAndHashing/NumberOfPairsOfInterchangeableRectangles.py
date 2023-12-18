# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratioMap = {}
        numOfInterchangeable = 0

        for rect in rectangles:
            ratio = rect[1] / rect[0]

            if ratio in ratioMap:
                ratioMap[ratio] += 1
                numOfInterchangeable += ratioMap[ratio]
            else:
                ratioMap[ratio] = 0

        return numOfInterchangeable
