from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None:
            slow = slow.next
            if fast.next is None:
                return False

            fast = fast.next.next

            if fast == slow:
                print(slow.val)
                return True
        return False


sol = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(sol.hasCycle(head))
