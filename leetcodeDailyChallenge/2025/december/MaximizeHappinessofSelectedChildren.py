# https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        # sort it in reverse
        # for each iteration i subtract iteration from current number
        # keep track of sum
        ans = 0
        for i in range(k):
            ans += max(happiness[i] - i, 0)
        return ans