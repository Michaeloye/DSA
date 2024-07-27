# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)

        for src, dst, curCost in zip(original, changed, cost):
            adj[src].append((dst, curCost))
        
        def dijkstra(src):
            heap = [(0, src)]
            minCostMap = {}

            while heap:
                cost, node = heapq.heappop(heap)

                if node in minCostMap:
                    continue
                
                minCostMap[node] = cost
                for nei, neiCost in adj[node]:
                    heapq.heappush(heap, (cost + neiCost, nei))

            return minCostMap

        minCostMaps = {c: dijkstra(c) for c in set(source)}
        res = 0

        for src, dst in zip(source, target):
            if dst not in minCostMaps[src]:
                return -1
            res += minCostMaps[src][dst]
        
        return res
