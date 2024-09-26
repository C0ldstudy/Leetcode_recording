class MyHashMap:

    def __init__(self):
        self.data = {}
        

    def put(self, key: int, value: int) -> None:
        # if not (key in self.data.keys()):
        #     self.data[key] = value
        # else:
        self.data[key] = value
        

    def get(self, key: int) -> int:
        if key in self.data.keys():
            return self.data[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.data.keys():
            self.data.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)