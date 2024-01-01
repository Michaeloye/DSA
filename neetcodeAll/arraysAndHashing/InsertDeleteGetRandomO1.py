# https://leetcode.com/problems/insert-delete-getrandom-o1

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class RandomizedSet:

    def __init__(self):
        self.space = 769
        self.set = [ListNode(0) for _ in range(self.space)]
        self.occupied = []

    def _hash(self, key):
        return key % self.space

    def insert(self, val: int) -> bool:
        curr = self.set[self._hash(val)]

        while curr and curr.next:
            if curr.next.key == val:
                return False
            curr = curr.next

        curr.next = ListNode(val)
        self.occupied.append(val)
        return True

    def remove(self, val: int) -> bool:
        curr = self.set[self._hash(val)]

        while curr and curr.next:
            if curr.next.key == val:
                curr.next = curr.next.next
                occupiedIndex = self.occupied.index(val)
                self.occupied.pop(occupiedIndex)
                return True
            curr = curr.next

        return False

    def getRandom(self) -> int:
        randomIdx = random.randint(0, len(self.occupied) - 1)

        return self.occupied[randomIdx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
