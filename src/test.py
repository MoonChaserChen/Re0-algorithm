from collections import deque
import threading


class MyStack:
    def __init__(self):
        self.lock = threading.RLock()
        self.dq = deque([])

    def push(self, x: int) -> None:
        with self.lock:
            le = len(self.dq)
            self.dq.append(x)
            for i in range(le):
                self.dq.append(self.dq.popleft())

    def pop(self) -> int:
        return self.dq.popleft()

    def top(self) -> int:
        return self.dq[0] if len(self.dq) > 0 else None

    def empty(self) -> bool:
        return len(self.dq) == 0
