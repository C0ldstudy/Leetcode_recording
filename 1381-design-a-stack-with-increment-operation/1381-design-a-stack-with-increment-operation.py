class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        # print(self.stack)
        if len(self.stack) < self.maxSize:
            self.stack = [x] + self.stack
        return
        
        

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            # print(self.stack)
            return self.stack.pop(0)
        

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) >= k:
            for i in range(1, k+1):
                self.stack[-i] += val
        else:
            for i in range(1, len(self.stack)+1):
                self.stack[-i] += val            
                
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)