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


# O(n) solution
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)

        if (2 * total) % len(skill):
            return -1

        target = (2 * total) // len(skill)
        countMap = {}
        ans = 0
        for num in skill:
            countMap[num] = 1 + countMap.get(num, 0)
        
        for num in skill:
            if not countMap[num]:
                continue

            diff = target - num
            if diff not in countMap or not countMap[diff]:
                return -1

            countMap[num] -= 1
            ans += num * diff
            countMap[diff] -= 1
        
        return ans
