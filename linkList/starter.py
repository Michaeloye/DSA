class Node:
    def __init__(self, val = -1, next = None):
      self.val = val
      self.next = next
    
    def __repr__(self):
      return f"Node({self.val})"

    def __str__(self):
      return f"Node({self.val})"


node2 = Node(2)
node4 = Node(4)
node5 = Node(5)

node2.next = node4
node4.next = node5
node5.next = None

print(node2, node2.next, node2.next.next, node2.next.next.next)

def arrayToLinkedList(arr):
  head = Node(arr[0])
  cur = head
  for i in arr[1:]:
    cur.next = Node(i)
    cur = cur.next
  
  cur.next = None
  return head

head = arrayToLinkedList([4,6,2,9,6])

print(head.next, head.next.next, head.next.next.next)
