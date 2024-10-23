# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0

        facing = 0 # 0 1 2 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        obstacles = {tuple(o) for o in obstacles}

        maxDistance = 0

        for command in commands:
            
            if command ==  -1:
                facing += 1
                facing %= 4

            if command == -2:
                facing -= 1
                facing %= 4

            else:
                dx, dy = directions[facing]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x = x + dx
                    y = y + dy
            distance = x**2 + y**2
            maxDistance = max(maxDistance, distance)

        return maxDistance