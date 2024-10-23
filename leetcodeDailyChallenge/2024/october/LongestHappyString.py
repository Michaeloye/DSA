# https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cMap = [(-a, "a"), (-b, "b"), (-c, "c")]
        res = ""
        maxHeap = []
        for count, c in cMap:
            if count:
                heapq.heappush(maxHeap, (count, c))

        while maxHeap:
            count, c = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == c:
                if not maxHeap:
                    break
                count2, c2 = heapq.heappop(maxHeap)

                res += c2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, c2))
            else:
                count += 1
                res += c
            if count:
                heapq.heappush(maxHeap, (count, c))

        return res
