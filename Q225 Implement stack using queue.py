class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        s1 = len(self.queue1)
        # Except element at the first
        while s1 > 1:
            self.queue2.append(self.queue1.popleft())
            s1 -= 1
        remove = self.queue1.popleft()
        # Swift queue2 to queue1
        self.queue1, self.queue2 = self.queue2, self.queue1
        return remove

    def top(self) -> int:
        end = len(self.queue1)
        return self.queue1[end - 1]

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()