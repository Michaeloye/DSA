# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(comb, openCnt, closeCnt):
            if openCnt > n or closeCnt > n:
                return
            if openCnt == closeCnt == n:
                ans.append("".join(comb))
                return
            # closeCnt should not be greater than openCnt
            # openCnt should not exceed n

            if closeCnt >= openCnt:
                comb.append("(")
                backtrack(comb, openCnt + 1, closeCnt)
                comb.pop()
            else:
                for p, od, cd in [("(", 1, 0), (")", 0, 1)]:
                    comb.append(p)
                    backtrack(comb, openCnt + od, closeCnt + cd)
                    comb.pop()

        backtrack([], 0, 0)
        return ans