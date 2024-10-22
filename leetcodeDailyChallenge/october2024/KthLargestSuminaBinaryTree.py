# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = deque([(root, 0)]) # (node, level)
        sumMap = {}
        while queue:
            cur, level = queue.popleft()
            sumMap[level] = cur.val + sumMap.get(level, 0)
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))

        sums= list(sumMap.values())
        sums.sort(reverse=True)

        if k > len(sums):
            return -1
        for i in range(len(sums)):
            if i + 1 == k:
                return sums[i]

# Another solution using Heap
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = deque([root])
        minHeap = []

        while queue:
            levelSum = 0

            for i in range(len(queue)):
                cur = queue.popleft()
                levelSum += cur.val

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            heapq.heappush(minHeap, levelSum)

            while len(minHeap) > k:
                heapq.heappop(minHeap)
        return -1 if len(minHeap) < k else minHeap[0]