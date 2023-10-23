from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        linkedListA = headA
        linkedListB = headB

        while linkedListA is not None:
            nodes.add(linkedListA)

            linkedListA = linkedListA.next

        while linkedListB is not None:
            if linkedListB in nodes:
                return linkedListB
            linkedListB = linkedListB.next

        return None
