# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums = [(n, i) for i, n in enumerate(nums)]
        heap = nums
        heapq.heapify(heap)

        seen = set()
        score = 0

        while heap:
            curNum, curIdx = heapq.heappop(heap)
            if curIdx in seen:
                continue
            seen.add(curIdx - 1)
            seen.add(curIdx)
            seen.add(curIdx + 1)
            score += curNum



        return score