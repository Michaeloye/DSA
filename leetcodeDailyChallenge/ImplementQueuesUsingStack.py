# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x) 

    def pop(self) -> int:
        poppedItem = self.queue.pop(0)
        return poppedItem

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not bool(len(self.queue))
