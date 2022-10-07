
class MyCalendarThree:

    def __init__(self):
        self.data = {}

    def book(self, start: int, end: int) -> int:
        if not start in self.data.keys():
            self.data[start] = 0
        if not end in self.data.keys():
            self.data[end] = 0     
        self.data[start] +=  1
        self.data[end] +=  -1
        self.data = dict(sorted(self.data.items()))
        result = 0
        current = 0
        for i in self.data.keys():
            current += self.data[i]
            if current > result:
                result = current
        return result



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)