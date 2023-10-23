from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        previous_node = None
        verdict = True

        while fast and fast.next:
            fast = fast.next.next

            next_node = slow.next
            slow.next = previous_node
            previous_node = slow

            slow = next_node

        if fast:
            slow = slow.next

        while slow and previous_node:
            if slow.val == previous_node.val:
                verdict = True
            else:
                verdict = False
                break

        return verdict


# class Solution1:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         slow = fast = head

#         previous_node = None
#         while fast and fast.next:
#             fast = fast.next.next

#             next_node = slow.next
#             slow.next = previous_node
#             previous_node = slow
#             slow = next_node

#         if fast:
#             slow = slow.next

#         while slow and slow.val == previous_node.val:
#             slow = slow.next
#             previous_node = previous_node.next

#         return slow is None
