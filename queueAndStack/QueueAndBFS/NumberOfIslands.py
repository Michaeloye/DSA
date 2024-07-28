class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        LEN_ROW = len(grid)
        LEN_COL = len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(LEN_ROW) and c in range(LEN_COL) and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        numberOfIslands = 0

        for r in range(LEN_ROW):
            for c in range(LEN_COL):
                # run bfs if not in visited and value is "1"
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    numberOfIslands += 1
        
        return numberOfIslands
