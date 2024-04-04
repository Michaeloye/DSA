# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenRows = len(board)
        lenCols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r, c) in path:
                return False
            if r < 0 or c < 0 or r >= lenRows or c >= lenCols or board[r][c] != word[i]:
                return False

            path.add((r, c))
            res = dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
            path.remove((r, c))

            return res
        
        for r in range(lenRows):
            for c in range(lenCols):
                if dfs(r, c, 0):
                    return True
                
        return False
