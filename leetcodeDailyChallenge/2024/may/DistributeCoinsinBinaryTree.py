# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur):
            if not cur:
                return 0
            
            lExtra = dfs(cur.left)
            rExtra = dfs(cur.right)

            extra = cur.val - 1 + lExtra + rExtra

            self.res += abs(extra)
            return extra

        dfs(root)
        return self.res