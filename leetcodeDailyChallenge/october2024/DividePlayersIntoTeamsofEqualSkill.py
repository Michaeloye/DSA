# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        l = 0
        r = len(skill) - 1
        target = skill[l] + skill[r]
        ans = 0

        while l < r:
            left = skill[l]
            right = skill[r]

            if left + right == target:
                ans += left * right
            else:
                return -1
            l += 1
            r -= 1
        
        return ans