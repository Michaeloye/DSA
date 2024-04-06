class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)]  for j in range(n)]
        ans = []
        
        def verifySpot(board, r, c):
            col = c
            while col >= 0:
                if board[r][col] == "Q":
                    return False
                col -= 1
            
            row = r
            col = c
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                col -= 1
                row -= 1
            
            row = r
            col = c
            while row < n and col >= 0:
                if board[row][col] == "Q":
                    return False
                col -= 1
                row += 1
            return True

        def dfs(c):
            if c >= n:
                res = []
                for row in board:
                    res.append("".join(row))
                ans.append(res)
                return

            for row in range(n):
                if verifySpot(board, row, c):
                    board[row][c] = "Q"
                    dfs(c + 1)
                    board[row][c] = "."

        dfs(0)
        return ans

