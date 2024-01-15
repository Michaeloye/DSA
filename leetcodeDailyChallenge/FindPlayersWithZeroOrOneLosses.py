# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnersSet = set()
        losersMap = {}
        ans = [[], []]

        for match in matches:
            winner, loser = match
            winnersSet.add(winner)
            losersMap[loser] = 1 + losersMap.get(loser, 0)

            if loser in winnersSet:
                winnersSet.remove(loser)
            if winner in losersMap:
                winnersSet.remove(winner)

        ans[0] = sorted(list(winnersSet))
        ans[1] = sorted([key for key in losersMap if losersMap[key] == 1])

        return ans
