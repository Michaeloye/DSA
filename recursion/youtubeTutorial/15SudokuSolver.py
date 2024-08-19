class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def solve():
            # handle solve board here
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == ".":
                        for n in range(1, 10):
                            n = str(n)
                            if isValid(r, c, n):
                                board[r][c] = n
                                
                                if solve() == True:
                                    return True
                                else:
                                    board[r][c] = "."
                        return False
            return True
        
        def isValid(r, c, num):
            # handle if the number is valid for that postion on the baord

            for i in range(9):
                # check row
                if board[r][i] == num:
                    return False
                # check ol
                if board[i][c] == num:
                    return False

                # check sub matrix
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == num:
                    return False

            return True

        solve()    