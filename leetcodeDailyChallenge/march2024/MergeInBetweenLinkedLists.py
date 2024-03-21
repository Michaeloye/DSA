# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pos = 0
        # track where a was found
        breakPos = pos
        curr1 = list1
        curr2 = list2
        rem = None

        while curr1 and curr1.next:
            if pos == a - 1:
                rem = curr1.next
                curr1.next = curr2
                breakPos = pos
            pos += 1
            curr1 = curr1.next
        while rem:
            if breakPos == b:
                curr1.next = rem
            breakPos += 1
            rem = rem.next
        return list1