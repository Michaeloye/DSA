# https://leetcode.com/problems/grid-game

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        preSum1 = [i for i in grid[0]]
        preSum2 = [i for i in grid[1]]

        for i in range(1, len(grid[0])):
            preSum1[i] += preSum1[i - 1]
            preSum2[i] += preSum2[i - 1]

        res = float("inf")

        for i in range(len(grid[0])):
            top = preSum1[-1] - preSum1[i]
            bottom = preSum2[i - 1] if i > 0 else 0

            maxPoints = max(top, bottom)
            res = min(res, maxPoints)

        return res


# first try using dfs approach
# reason why it won't work: https://leetcode.com/problems/grid-game/solutions/1486340/c-java-python-robot1-minimize-topsum-and-bottomsum-of-robot-2-picture-explained/
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        graph = {}
        visited = {}

        for i in range(len(grid)):
            subArr = grid[i]
            for j in range(len(subArr)):
                numLoc = (i, j)
                graph[numLoc] = []
                visited[numLoc] = False

                if i + 1 < len(grid):
                    graph[numLoc].append(tuple([i + 1, j]))
                if j + 1 < len(subArr):
                    graph[numLoc].append(tuple([i, j + 1]))

        storeDfs = []
        start = (0, 0)
        nodes = []
        maxPoint = grid[0][0]

        def dfs(node, maxPoint):
            pathA = []

            print(node)
            visited[node] = True
            nodes.append(node)
            # print(visited)
            # traverse all neighbours
            for _node in graph[node]:
                dfs(_node, maxPoint)
                # if not visited[_node] and not _node == (1, len(grid[0]) - 1):
                #     # print(grid[_node[0]][_node[1]])
                #     maxPoint += grid[_node[0]][_node[1]]
                #     # print(maxPoint)
                #     dfs(_node, maxPoint)
                #     # maxPoint

        dfs(start, maxPoint)

        print(visited)
        return 4
