# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# UNOPTIMIZED SOLUTION
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ancestors = []
        maxDifference = 0

        def dfs(node, anc, diff):
            if not node:
                return diff

            for num in anc:
                diff = max(abs(node.val - num), diff)
            anc.append(node.val)
            l = dfs(node.left, anc, diff)
            r = dfs(node.right, anc, diff)
            if len(anc):
                anc.pop()
            return (max(l, r))

        ans = dfs(root, ancestors, maxDifference)
        return ans


# OPTIMIZED SOLUTION


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node, minVal=float('inf'), maxVal=float('-inf')):
            if not node:
                return maxVal - minVal

            minVal = min(node.val, minVal)
            maxVal = max(node.val, maxVal)
            l = dfs(node.left, minVal, maxVal)
            r = dfs(node.right, minVal, maxVal)

            return max(l, r)

        return dfs(root)
