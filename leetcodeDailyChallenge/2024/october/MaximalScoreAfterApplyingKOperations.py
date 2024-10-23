# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        maxHeap = [-1 * n for n in nums]
        heapq.heapify(maxHeap)
        
        while k > 0:
            maxNum = heapq.heappop(maxHeap)
            maxNum = -1 * maxNum

            updatedMax = ceil(maxNum / 3)
            score += maxNum
            heapq.heappush(maxHeap, updatedMax * -1)
            k -= 1
        return score