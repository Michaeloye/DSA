from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        stash = cur

        while cur is not None:
            stash = cur.next

            cur.next = prev
            prev = cur

            cur = stash

        return prev
