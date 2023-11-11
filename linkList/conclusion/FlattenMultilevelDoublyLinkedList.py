"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/discuss/152725/Python-solution-with-explanation


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        stack = []

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            else:
                if not curr.next and len(stack):
                    temp = stack.pop()
                    temp.prev = curr
                    curr.next = temp

            curr = curr.next
        return head


# another solution: recursive solution
# class Solution:
#     def flatten(self, head):

#         def flatten(head):
#             last = head
#             while head:
#                 next_node, last = head.next, head
#                 if head.child:
#                     last = flatten(head.child)
#                     head.next = head.child
#                     head.child.prev = head
#                     last.next = next_node
#                     if next_node:
#                         next_node.prev = last
#                     head.child = None
#                 head = next_node
#             return last

#         flatten(head)
#         return head
