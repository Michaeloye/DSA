# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            leftDiff = dfs(node.left)
            rightDiff = dfs(node.right)

            for ld in leftDiff:
                for rd in rightDiff:
                    if ld + rd <= distance:
                        self.pairs += 1

            totalDiff = leftDiff + rightDiff

            return [d + 1 for d in totalDiff]

        dfs(root)
        return self.pairs