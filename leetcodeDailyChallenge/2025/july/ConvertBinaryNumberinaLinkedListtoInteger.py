# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def binaryToDecimal(binary):
            n = len(binary) - 1
            ans = 0

            for c in binary:
                ans += int(c) * (2 ** n)
                n -= 1

            return ans

        binary = []
        while head:
            binary.append(head.val)
            head = head.next

        return binaryToDecimal(binary)