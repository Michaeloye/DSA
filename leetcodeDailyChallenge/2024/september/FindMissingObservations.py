# https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        N = len(rolls) + n
        rollSum = sum(rolls)
        totalSum = mean * N
        missingSum = totalSum - rollSum

        if missingSum  < 1 * n or missingSum > 6 * n:
            return []

        ans = []

        while n > 0:
            maxChoice = missingSum - n + 1

            roll = min(6, maxChoice)
            missingSum -= roll
            n -= 1
            ans.append(roll)
        
        return ans