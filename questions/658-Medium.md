### 658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # deal with the situations that x is the smallest or largest number
        if (x <= arr[0]):
            return arr[:k]
        elif (x >= arr[-1]):
            return arr[-k:]
        else:
        # calculate the distance of the elements with x
            new_arr = []
            for item in arr:
                new_arr.append(abs(item-x))
            index = self.argsort(new_arr)[:k]#.sort()
            index.sort()
            result = []
            for i in index:
                result.append(arr[i])
            return result

    def argsort(self, seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
        return sorted(range(len(seq)), key=seq.__getitem__)
```
