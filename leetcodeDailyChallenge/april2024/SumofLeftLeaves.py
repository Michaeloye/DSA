# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, isLeft):
            if not node:
                return 0
            if not node.left and node.right:
                if isLeft:
                    return node.val
                else:
                    return 0
            
            leftSum = dfs(node.left, True)
            rightSum = dfs(node.right, False)

            return leftSum + rightSum

        return dfs(root, False)