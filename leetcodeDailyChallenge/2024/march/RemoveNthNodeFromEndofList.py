# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        n = length - n
        
        position = 1
        _head = head

        while _head:
            if n == 0:
                head = _head.next
                return head
            elif position == n:
                curr = _head
                nextNodes = curr.next.next
                nodeToBeRemoved = curr.next
                nodeToBeRemoved.next = None
                curr.next = nextNodes
                return head

            _head = _head.next
            position += 1
        
        return _head