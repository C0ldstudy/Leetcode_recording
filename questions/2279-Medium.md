### 2279. Maximum Bags With Full Capacity of Rocks
You have `n` bags numbered from `0` to `n - 1`. You are given two **0-indexed** integer arrays `capacity` and `rocks`. The ith bag can hold a maximum of `capacity[i]` rocks and currently contains `rocks[i]` rocks. You are also given an integer `additionalRocks`, the number of additional rocks you can place in **any** of the bags.

Return the **maximum** number of bags that could have full capacity after placing the additional rocks in some bags.

 ### Key idea
 - sort the array and greedy algorithm

### Solution
```python
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        length = len(capacity)
        for i in range(length):
            capacity[i] -= rocks[i]
        capacity = sorted(capacity)
        count = 0
        for i in capacity:
            if additionalRocks <= 0 : return count
            if i == 0:
                count += 1
                continue
            elif i <= additionalRocks:
                count += 1
                additionalRocks -= i
        return count

```
