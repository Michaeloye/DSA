# https://leetcode.com/problems/smallest-string-starting-from-leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def helper(node, cur):
            if not node:
                return

            cur = chr(ord('a') + node.val) + cur

            if node.left and node.right:
                return min(helper(node.left, cur), helper(node.right, cur))
            if node.left:
                return helper(node.left, cur)
            if node.right:
                return helper(node.right, cur)

            return cur

        return helper(root, "")