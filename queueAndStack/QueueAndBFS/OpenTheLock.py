class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []

            for i in range(len(lock)):
                up = str((int(lock[i]) + 1) %10)
                res.append(lock[:i] + up + lock[i+1:])
                down = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + down + lock[i+1:])
            return res
                
        queue = deque()
        visited = set(deadends)

        queue.append(("0000", 0)) # lock, moves        
        
        while queue:
            curLock, moves = queue.popleft()
            
            if curLock == target:
                return moves
            
            for child in children(curLock):
                if child in visited:
                    continue
                queue.append((child, moves + 1))
                visited.add(child)
        
        return -1