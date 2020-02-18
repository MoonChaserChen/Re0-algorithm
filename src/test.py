class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.val_stack = []


    def push(self, x: int) -> None:
        if not self.min_stack or x <= self.min_stack[-1]: self.min_stack.append(x)
        self.val_stack.append(x)

    def pop(self) -> int:
        v = self.val_stack.pop()
        if self.min_stack and v == self.min_stack[-1]:
            self.min_stack.pop()
        return v

    def top(self) -> int:
        if self.val_stack: return self.val_stack[-1]

    def get_min(self) -> int:
        if self.min_stack: return self.min_stack[-1]