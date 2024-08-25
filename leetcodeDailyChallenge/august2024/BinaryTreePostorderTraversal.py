# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# post order traversal
class Solution:
    # left -> right -> root
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans

# pre order traversal
class Solution:
    # root -> left -> right
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return

            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

# in order traversal
class Solution:
    # left -> root -> right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans