# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []

        def dfs(node, combination):
            if not node:
                return
            
            combination.append(str(node.val))

            if not node.left and not node.right:
                numbers.append(combination[:])

            dfs(node.left, combination)
            dfs(node.right, combination)

            combination.pop()
        
        dfs(root, [])

        totalSum = 0

        for i in range(len(numbers)):
            totalSum += int("".join(numbers[i]))


        return totalSum

# Another solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, currSum):
            if not node:
                return 0
            
            currSum = currSum * 10 + node.val

            if not node.left and not node.right:
                return currSum
            else:
                return dfs(node.left, currSum) + dfs(node.right, currSum)
        
        return dfs(root, 0)