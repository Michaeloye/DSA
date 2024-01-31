# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjList = {}

        # CONVERT TREE TO ADJACENCY LIST (GRAPH) SO WE CAN RUN BFS ON IT
        def dfs(node, parentVal, adjLs):
            if not node:
                return

            adjLs[node.val] = set()
            if node.left:
                adjLs[node.val].add(node.left.val)
            if node.right:
                adjLs[node.val].add(node.right.val)
            if parentVal is not None:

                adjLs[node.val].add(parentVal)

            dfs(node.left, node.val, adjLs)
            dfs(node.right, node.val, adjLs)

        dfs(root, None, adjList)

        def bfs(graph):
            q = [start]
            vis = set()
            res = -1

            while len(q):
                res += 1
                for _ in range(len(q)):
                    i = q.pop(0)
                    vis.add(i)
                    for j in graph[i]:
                        if j not in vis:
                            q.append(j)
            return res

        return bfs(adjList)
