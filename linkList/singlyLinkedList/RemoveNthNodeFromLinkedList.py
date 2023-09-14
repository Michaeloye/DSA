from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        length = 0

        while fast is not None:
            fast = fast.next
            length += 1

        index = length - n

        if (length == 0):
            return head

        if (index >= 0 and index < length):

            prev = head

            if (index == 0):
                head = prev.next
                length -= 1
                return head

            for i in range(1, index):
                prev = prev.next

            cur = prev.next
            next = cur.next

            prev.next = next
            cur.next = None
            length -= 1

        return head
