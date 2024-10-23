# https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque([root])
        levelSums = []

        while q:
            levelSum = 0
            for i in range(len(q)):
                cur = q.popleft()

                levelSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            levelSums.append(levelSum)
        
        def dfs(node, depth):
            if not node:
                return
            # check children of current node
            if node.left or node.right:
                left = node.left.val if node.left else 0
                right = node.right.val if node.right else 0
                childrenSum = left + right
                if node.left:
                    node.left.val = levelSums[depth + 1] - childrenSum
                if node.right:
                    node.right.val = levelSums[depth + 1] - childrenSum

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        root.val = 0
        return root

            