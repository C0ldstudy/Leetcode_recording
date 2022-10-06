class TimeMap:

    def __init__(self):
        self.data = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        # save [key, value] as an array item. For empty items, use ['', '']
        if timestamp > len(self.data):
            for i in range(len(self.data), timestamp):
                self.data.append(['', ''])
        self.data[timestamp-1] = [key, value]
    
    def get(self, key: str, timestamp: int) -> str:
        # use reverse order to return the result
        start = min(timestamp, len(self.data))
        # print(timestamp, len(self.data))
        for i in range(start-1, -1, -1):
            if self.data[i][0] == key:
                return self.data[i][1]
        return ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)