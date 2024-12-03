# https://leetcode.com/problems/adding-spaces-to-a-string/

class listNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        head = listNode("0")
        cur = head
        spaces = set(spaces)

        # create linked list
        for c in s:
            cur.next = listNode(c)
            cur = cur.next
        
        # add " " to linked list
        cur = head
        count = -1

        while cur.next:
            seen = False
            if count + 1 in spaces:
                newNode = listNode(" ")
                newNode.next = cur.next
                cur.next = newNode
                seen = True
            if seen:
                cur = cur.next.next
            else:
                cur = cur.next
            count += 1
        
        ans = ""
        head = head.next
        while head:
            ans += head.val
            head = head.next

        return ans


# another solution
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = [c for c in s]
        splits = []
        spaces = set(spaces)
        l = 0

        for r in range(len(s)):
            if r in spaces:
                splits.append("".join(s[l:r]))
                l = r
        splits.append("".join(s[l:r + 1]))
        return " ".join(splits)
