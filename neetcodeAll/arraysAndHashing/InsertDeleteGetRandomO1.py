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

# SECOND SOLUTION
class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numArray = []

    def insert(self, val: int) -> bool:
        res = val in self.hashMap

        if not res:
            self.numArray.append(val)
            self.hashMap[val] = len(self.numArray) - 1

        return not res

    def remove(self, val: int) -> bool:
        res = val in self.hashMap

        if res:
            idx = self.hashMap[val]
            lastItem = self.numArray[-1]
            self.numArray[idx] = lastItem
            self.numArray.pop()

            self.hashMap[lastItem] = idx
            del self.hashMap[val]
        return res

    def getRandom(self) -> int:
        randomNum = random.randint(0, len(self.numArray) - 1)

        return self.numArray[randomNum]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
