# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10**5)
        num = ""
        curr = head
        while curr:
            num += str(curr.val)
            curr = curr.next
        
        doubNum = str(int(num) * 2)

        newHead = ListNode()
        dummy = newHead

        for num in doubNum:
            dummy.next = ListNode(int(num))
            dummy = dummy.next

        return newHead.next