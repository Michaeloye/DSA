# https://leetcode.com/problems/design-hashmap

class ListListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.space = 769
        self.map = [ListListNode(-1, -1) for _ in range(self.space)]

    def _hash(self, key):
        return key % self.space

    def put(self, key: int, value: int) -> None:
        curr = self.map[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = ListListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.map[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        curr = self.map[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
