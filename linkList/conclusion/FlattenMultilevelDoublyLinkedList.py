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
