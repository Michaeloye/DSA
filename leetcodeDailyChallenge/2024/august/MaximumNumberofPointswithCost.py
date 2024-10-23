# https://leetcode.com/problems/maximum-number-of-points-with-cost/

# BRUTE FORCE SOLUTION
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])

        for r in range(ROWS):
            if r == 0:
                continue
            prevRow = points[r - 1]

            for c in range(COLS):
                maxDiff = 0

                for pc in range(COLS):
                    maxDiff = max(
                        maxDiff, 
                        points[r][c] + prevRow[pc] - abs(pc - c)
                    )
                points[r][c] = maxDiff
        
        return max(points[-1])


# DP SOLUTION
class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
      ROWS = len(points)
      COLS = len(points[0])

      row = points[0]

      for r in range(1, ROWS):
          nextRow = points[r].copy()
          left = [0] * COLS
          right = [0] * COLS

          left[0] = row[0]

          for c in range(1, COLS):
              left[c] = max(row[c], left[c - 1] - 1)

          right[COLS - 1] = row[COLS - 1]
          for c in range(COLS - 2, -1, -1):
              right[c] = max(row[c], right[c + 1] - 1)
          
          for c in range(COLS):
              nextRow[c] += max(left[c], right[c])
          row = nextRow

      return max(row)
