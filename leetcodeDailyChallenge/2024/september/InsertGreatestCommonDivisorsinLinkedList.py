# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(a,b):
            while b:
                a,b = b , a%b
            return a 

        curr = head

        while curr and curr.next:
            a = curr.val
            b = curr.next.val

            gcd = GCD(a, b)
            prev = curr.next
            gcdNode = ListNode(gcd, prev)

            curr.next = gcdNode
            curr = prev
        
        return head