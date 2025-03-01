# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.resolveTree(self.root)
    
    def resolveTree(self, node):
        if not node:
            return
        if node.left:
            node.left.val = 2 * node.val + 1
            self.resolveTree(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.resolveTree(node.right)
        return
    def dfs(self, node, target):
        if not node:
            return False
        if node.val == target:
            return True

        return self.dfs(node.left, target) or self.dfs(node.right, target)

    def find(self, target: int) -> bool:
        
        return self.dfs(self.root, target)
    

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)