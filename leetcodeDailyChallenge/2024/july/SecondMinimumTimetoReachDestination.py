# https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        q = deque([1])
        curTime = 0
        res = -1
        visitTimes = defaultdict(list)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return curTime
                    res = curTime
                for nei in adj[node]:
                    neiTimes = visitTimes[nei]
                    if len(neiTimes) == 0 or (len(neiTimes) == 1 and neiTimes[0] != curTime):
                        q.append(nei)
                        neiTimes.append(curTime)

            if (curTime // change) % 2 == 1:
                curTime += change - (curTime  % change)
            curTime += time
