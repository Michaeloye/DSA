class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0 

    def get(self, index: int) -> int:
        if(index < 0 or index > self.length):
            return -1
        if (self.length == 0):
            return -1
        
        cur = self.head
        for i in range(self.length):
            if (i == index):
                return cur.val

            cur = cur.next

    def addAtHead(self, val: int) -> None:
        curHead = self.head
        if(self.length == 0):
            self.head = Node(val)
        else:
            newHead = Node(val)
            newHead.next = curHead
            self.head = newHead
        
        self.length += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        newTail=Node(val)
        if(cur == None):
          cur = newTail

        for i in range(self.length):
            if (cur.next == None):
                cur.next = newTail
                self.length += 1
                return

            cur = cur.next

        # self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if(index == 0):
            self.addAtHead(val)
            return

        if(index == self.length - 1):
            self.addAtTail(val)
            return

        if(index >= self.length):
            return

        prev = self.head
        newNode = Node(val)

        # starting at 1 since we already have prev which is our head
        for i in range(1, self.length):
            if (i == index):
                next = prev.next
                prev.next = newNode
                newNode = next
                self.length += 1
                return
            prev = prev.next
        

    def deleteAtIndex(self, index: int) -> None:
        print(self.head)
        if(self.length == 0):
            return

        if (index >=0 and index < self.length):

            prev = self.head

            for i in range(1, self.length):
                if(i == index):
                    cur = prev.next
                    next = cur.next
                    
                    prev.next = next
                    cur.next = None
                    self.length -= 1
                    return
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(1)
# obj.addAtTail(2)
# obj.addAtIndex(1,2)
# obj.deleteAtIndex(1)