# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        # reverse second
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first = head
        second = prev

        # merge
        while second:
            next1 = first.next
            next2 = second.next
            first.next = second
            second.next = next1
            first = next1
            second = next2
