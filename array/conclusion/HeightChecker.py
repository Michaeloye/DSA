from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        output = 0
        expected = heights[:]
        expected.sort()

        for i in range(len(heights)):
            if (heights[i] != expected[i]):
                output += 1

        return output


soln = Solution()
heights = [1, 1, 4, 2, 1, 3]
print(soln.heightChecker(heights))
