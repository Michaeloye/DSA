# https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ROWS = len(grid)
        COLS = len(grid[0])

        n = len(grid)
        nums = set([i for i in range(1, n * n + 1)])
        ans = [0, 0]

        for r in range(ROWS):
            for c in range(COLS):
                num = grid[r][c]
                if num in nums:
                    nums.remove(num)
                else:
                    ans[0] = num
        nums = list(nums)
        ans[1] = nums[0]
        return ans

# ANOTHER SOLUTION O(1) space
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ROWS = len(grid)
        COLS = len(grid[0])
        n = len(grid)

        curSum = (1 + n * n) * (n * n)/2 # Sum of arithmetic progression (e, g 1 to 9)
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                num = grid[r][c]
                if num in seen:
                    dup = num
                else:
                    seen.add(num)
                    curSum -= num
                
        return [dup, int(curSum)]
