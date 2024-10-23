# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adjList = defaultdict(list)

        for i in range(len(edges)):
            src, dst = edges[i]
            prob = succProb[i]

            adjList[src].append([dst, prob])
            adjList[dst].append([src, prob])

        q = [(-1, start_node)]
        visited = set()
        while q:
            prob, curNode = heapq.heappop(q)
            visited.add(curNode)

            if curNode == end_node:
                return -1 * prob

            else:
                for node, p in adjList[curNode]:
                    if node not in visited:
                        heapq.heappush(q, (prob * p, node))

        return 0