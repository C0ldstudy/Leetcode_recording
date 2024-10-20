class MovingAverage:

    def __init__(self, size: int):
        self.data = [0] * size
        self.cnt = 0
        

    def next(self, val: int) -> float:
        if all(self.data):
            self.data.pop(0)
            self.data.append(val)
            # print(self.data)
            return sum(self.data)/self.cnt
        else:
            self.cnt += 1
            self.data[self.cnt-1] = val
            # print(self.data)
            
            return sum(self.data)/self.cnt
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)