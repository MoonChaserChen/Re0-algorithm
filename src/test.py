from collections import deque


class MyQueue:
    def __init__(self):
        self.stack1 = deque([])
        self.stack2 = deque([])
        self.first = None # stack1 栈底元素

    def push(self, x: int) -> None:
        if not self.stack1: self.first = x
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2: return self.stack2[-1]
        return self.first

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
