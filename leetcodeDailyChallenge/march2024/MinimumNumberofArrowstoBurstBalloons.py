# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]
            a, b = curr

            if a <= prev[1]:
                prev = [a, min(prev[1], b)]
                count -= 1
            else:
                prev = curr

        return count