# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, ans):
            if not node:
                ans.append(None)
                return
            
            ans.append(node.val)

            dfs(node.left, ans)
            dfs(node.right, ans)

        ansOne = []
        dfs(p, ansOne)

        ansTwo = []
        dfs(q, ansTwo)

        print(ansOne, ansTwo)
        return ansOne == ansTwo
