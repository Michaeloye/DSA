# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        resSet = set([root])

        def dfs(node):
            if not node:
                return None
            res = node

            if node.val in toDelete:
                res = None
                resSet.discard(node)

                if node.left: resSet.add(node.left)
                if node.right: resSet.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return res
        
        dfs(root)
        return list(resSet)