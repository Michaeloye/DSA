from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checkedNodes = set()
        slow = head

        while slow is not None:
            checkedNodes.add(slow)

            if (slow.next in checkedNodes):
                return slow.next

            slow = slow.next
        return None


sol = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(sol.detectCycle(head))
