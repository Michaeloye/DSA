# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        countMap = {}
        ans = 0

        for a, b in dominoes:
            if b <= a:
                a, b = b, a
            key = (a, b)
            ans += countMap[key] if key in countMap else 0
            countMap[key] = 1 + countMap.get(key, 0)

        return ans