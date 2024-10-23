# https://leetcode.com/problems/count-number-of-teams

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for m in range(1, len(rating) - 1):
            leftSmaller = 0
            rightBigger = 0

            for i in range(m):
                if rating[i] < rating[m]:
                    leftSmaller += 1
            for j in range(m + 1, len(rating)):
                if rating[j] > rating[m]:
                    rightBigger += 1

            res += leftSmaller * rightBigger
            leftBigger = m - leftSmaller
            rightSmaller = len(rating) - m - 1 - rightBigger

            res += leftBigger * rightSmaller
        return res