class MyQueue:

    def __init__(self):
        self.data = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        

    def pop(self) -> int:
        res = self.data[0]
        self.data = self.data[1:]
        return res
        

    def peek(self) -> int:
        return self.data[0]
        

    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()