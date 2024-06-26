# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val == 1
        
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)

# iterative* solution
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        value = {} # node: value

        while stack:
            node = stack.pop()

            if not node.left:
                value[node] = node.val == 1

            else:
                # node in value
                if node.left in value:
                    if node.val == 2:
                        value[node] = value[node.left] or value[node.right]
                    elif node.val == 3:
                        value[node] = value[node.left] and value[node.right]
                else:
                    stack.extend([node, node.left, node.right])

        return value[root]