# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 32

        for n in candidates:
            i = 0
            while n:
                count[i] += 1 & n
                i += 1
                n = n >> 1
        return max(count)