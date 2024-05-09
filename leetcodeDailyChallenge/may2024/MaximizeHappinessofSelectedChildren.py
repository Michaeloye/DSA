# https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        count = 0
        total = 0

        while k and happiness:
            child = happiness.pop()
            total += child - count if child - count > 0 else 0
            count += 1
            k -= 1
        
        return total