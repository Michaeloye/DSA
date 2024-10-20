# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if self.popStack:
            return self.popStack.pop()

        # populate popStack if empty
        while self.pushStack:
            top = self.pushStack.pop()
            self.popStack.append(top)
        
        return self.popStack.pop() if self.popStack else None
        

    def peek(self) -> int:
        if self.popStack:
            top = self.popStack.pop()
            self.popStack.append(top)
            return top
        
        # populate popStack if empty
        while self.pushStack:
            top = self.pushStack.pop()
            self.popStack.append(top)
        
        if self.popStack:
            top = self.popStack.pop()
            self.popStack.append(top)
            return top
        return None

    def empty(self) -> bool:
        if not self.pushStack and not self.popStack:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()