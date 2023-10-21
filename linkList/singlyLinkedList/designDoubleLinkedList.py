class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if (index < 0 or index >= self.length):
            return -1
        if self.head is None:
            return -1

        cur = self.head

        for i in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        newHead = Node(val)
        curHead = self.head

        if (curHead is None):
            self.head = newHead
        else:
            newHead.next = curHead
            curHead.prev = newHead
            self.head = newHead

        self.length += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        newTail = Node(val)
        if (cur == None):
            self.head = newTail
            self.length += 1
            return

        while cur.next is not None:
            cur = cur.next

        newTail.prev = cur
        cur.next = newTail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if (index == 0):
            self.addAtHead(val)
            return

        if (index == self.length):
            self.addAtTail(val)
            return

        if (index >= self.length):
            return

        former = self.head
        newNode = Node(val)

        # starting at 1 since we already have prev which is our head
        for i in range(1, index):
            former = former.next
        next = former.next
        # cur
        newNode.prev = former
        former.next = newNode

        next.prev = newNode
        newNode.next = next

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if (self.length == 0):
            return

        if (index >= 0 and index < self.length):

            former = self.head

            if (index == 0):
                self.head = former.next
                former.prev = None
                self.length -= 1
                return

            for i in range(1, index):
                former = former.next

            cur = former.next
            next = cur.next

            former.next = next

            cur.next = None
            cur.prev = None
            self.length -= 1

        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
