# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get the lenght of list
        cur = head
        n = 0

        while cur:
            n += 1
            cur = cur.next
        
        remShare = n % k
        ans = []
        if n // k <= 0:
            while k:
                if not head:
                    ans.append(None)
                else:
                    ans.append(ListNode(head.val))
                    head = head.next
                k -= 1
            return ans

        while head:
            extra = 1 if remShare else 0 
            share = (n // k) + extra
            newNode = ListNode(0)
            remShare = remShare - 1 if remShare else 0
            ref = newNode

            while share and head:
                newNode.next = ListNode(head.val)
                newNode = newNode.next

                share -= 1 
                if share == 0:
                    continue
                head = head.next
            if head:
                head = head.next
            ans.append(ref.next)

        return ans