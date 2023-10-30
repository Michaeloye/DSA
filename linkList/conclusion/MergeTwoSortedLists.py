from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(0)
        cur = mergedList

        while list1 or list2:
            if (list1 and list2):
                if (list1.val < list2.val):
                    mergedList.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    mergedList.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                mergedList.next = ListNode(list1.val)
                list1 = list1.next
            else:
                mergedList.next = ListNode(list2.val)
                list2 = list2.next
            mergedList = mergedList.next

        return cur.next
