# https://leetcode.com/problems/add-one-row-to-tree/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val, root)

        currDepth = 1

        queue = deque([root])

        while queue:
            if currDepth == depth - 1:
                break

            for _ in range(len(queue)):
                currNode = queue.popleft()
                print(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            currDepth += 1

        for node in queue:
            leftNode = node.left
            node.left = TreeNode(val, leftNode)

            rightNode = node.right
            node.right = TreeNode(val, None, rightNode)

        return root