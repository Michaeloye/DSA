# https://leetcode.com/problems/largest-triangle-area/

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        N = len(points)

        for i in range(N):
            for j in range(i, N):
                for k in range(j, N):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    cur_area = abs(x1 * (y2 - y3) - y1 * (x2 - x3) + (x2 * y3 - y2 *x3))
                    max_area = max(max_area, cur_area)
        return 0.5 * max_area


# OR
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        N = len(points)

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    AB = (x2 - x1, y2 - y1)
                    AC = (x3 - x1, y3 - y1)

                    cur_area = abs(AB[0] * AC[1] - AB[1] * AC[0])
                    max_area = max(max_area, cur_area)
        return 0.5 * max_area