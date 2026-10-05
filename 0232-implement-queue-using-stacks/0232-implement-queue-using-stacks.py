class MyQueue:

    def __init__(self):
        self.st=[]
        self.st2=[]

    def push(self, x: int) -> None:
            self.st.append(x)
    def pop(self) -> int:
        for _ in range(len(self.st)):
            self.st2.append(self.st.pop())
        v = self.st2.pop()
        for _ in range(len(self.st2)):
            self.st.append(self.st2.pop())
        return v

    def peek(self) -> int:
        for _ in range(len(self.st)):
            self.st2.append(self.st.pop())
        v = self.st2[-1]
        for _ in range(len(self.st2)):
            self.st.append(self.st2.pop())
        return v

    def empty(self) -> bool:
        return not self.st


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()