# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        i = head

        while i:
            while stack and stack[-1] < i.val:
                stack.pop()
            stack.append(i.val)
            i = i.next
        head = ListNode(stack[0]) if stack else None
        dub = head

        if len(stack) > 1:
            for num in stack[1:]:
                dub.next = ListNode(num)
                dub = dub.next
            
        return head