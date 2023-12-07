class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnMap = {i: set() for i in range(0, 9)}
        boxSet = {i: set() for i in range(0, 3)}

        for i, row in enumerate(board):
            numsSet = set()
            box = i % 3

            if box == 0:
                boxSet = {i: set() for i in range(0, 3)}
            for idx, num in enumerate(row):
                if num == ".":
                    continue
                if num in numsSet or num in columnMap[idx] or num in boxSet[idx // 3]:
                    return False

                else:
                    numsSet.add(num)
                    columnMap[idx].add(num)
                    boxSet[idx // 3].add(num)

        return True
