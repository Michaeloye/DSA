# https://leetcode.com/problems/design-hashset

# first attempt
class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        for i in self.hashSet:
            if i == key:
                return
        self.hashSet.append(key)

    def remove(self, key: int) -> None:
        for (idx, item) in enumerate(self.hashSet):
            if item == key:
                self.hashSet.pop(idx)
                break

    def contains(self, key: int) -> bool:
        for i in self.hashSet:
            if i == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# optimized attempt
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.space = 769
        self.set = [ListNode(0) for _ in range(self.space)]

    def _hash(self, key):
        return key % self.space

    def add(self, key: int) -> None:
        curr = self.set[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# optimized solution, using linked list
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.space = 769
        self.set = [ListNode(0) for _ in range(self.space)]

    def _hash(self, key):
        return key % self.space

    def add(self, key: int) -> None:
        curr = self.set[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[self._hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
