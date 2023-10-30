from typing import Optional
from singlyLinkedList import ListNode

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        concatedL1 = ""
        concatedL2 = ""
        resultOfAddition = 0
        linkedListResult = ListNode(0)
        dummy = linkedListResult

        while l1:
            concatedL1 += str(l1.val)
            l1 = l1.next

        while l2:
            concatedL2 += str(l2.val)
            l2 = l2.next

        resultOfAddition = str(int(concatedL1[::-1]) + int(concatedL2[::-1]))
        resultOfAddition = resultOfAddition[::-1]

        for i in resultOfAddition:
            linkedListResult.next = ListNode(i)
            linkedListResult = linkedListResult.next
        return dummy.next
