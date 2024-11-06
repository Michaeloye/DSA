# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        visited = set()
        queue = deque([]) #(r, c, minute)
        orange_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    orange_count += 1
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        time = 0
        while queue:
            cur_r, cur_c, cur_m = queue.popleft()
            time = max(time, cur_m)
            for dr, dc in dirs:
                r = cur_r + dr
                c = cur_c + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS:
                    if (r, c) not in visited and grid[r][c] == 1:
                        queue.append((r, c, cur_m + 1))
                        visited.add((r, c))

        return time if len(visited) == orange_count else -1
