# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/discuss/757913/Python-100-or-Recursive-Deepcopy
# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/discuss/4249215/Beats-99-or-O(-n-)-or-Easy-To-Understand-or-Python-(Step-by-step-explanation)
# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/discuss/4003617/Beats-100!-With-proper-explanation!


from typing import Optional
from singlyLinkedList import ListNode
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nodeMap = {None: None}
        curr = head

        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node = nodeMap[curr]
            node.next = nodeMap[curr.next]
            node.random = nodeMap[curr.random]
            curr = curr.next

        return nodeMap[head]
