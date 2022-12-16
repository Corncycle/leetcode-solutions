from collections import deque

class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        helper = deque()
        while self.stack:
            helper.append(self.stack.pop())
        self.stack.append(x)
        while helper:
            self.stack.append(helper.pop())        

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        x = self.pop()
        self.stack.append(x)
        return x

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()