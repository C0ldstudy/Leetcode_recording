The original method I tried is like this:
​
```python
class MyCalendarThree:
def book(self, start: int, end: int) -> int:
if end > len(self.data):
for i in range(len(self.data), end, 1):
self.data.append(0)
for i in range(start, end):
self.data[i] += 1
return max(self.data)
```
But the problem is that it cost too much storage to keep all the number. Now the method just use a dictionary to save the boundary and use `1` and `-1` to show the increment and decrement.