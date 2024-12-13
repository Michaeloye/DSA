# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-n for n in gifts]
        heapq.heapify(maxHeap)

        for _ in range(k):
            maxNum = -1 * heapq.heappop(maxHeap)
            sqrt = floor(maxNum ** 0.5)
            heapq.heappush(maxHeap, -sqrt)
        
        return -1 * sum(maxHeap)