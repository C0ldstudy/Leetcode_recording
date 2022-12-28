### 1962. Remove Stones to Minimize the Total
You are given a **0-indexed** integer array `piles`, where `piles[i]` represents the number of stones in the `ith` pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

Choose any `piles[i]` and **remove** `floor(piles[i] / 2)` stones from it.
**Notice** that you can apply the operation on the **same** pile more than once.

Return the **minimum** possible total number of stones remaining after applying the k operations.

`floor(x)` is the **greatest** integer that is **smaller** than or **equal** to `x` (i.e., rounds `x` down).
### Key idea
- Use heap




### Solution
Time Limit Exceeded
```python
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        length = len(piles)
        sum_number = sum(piles)
        for i in range(k):
            max_item = max(piles)
            max_index = piles.index(max_item)
            piles[max_index] = max_item - floor(max_item/2)
            sum_number -= floor(max_item/2)
            if sum_number < 1:
                return 0
        return sum_number
```

```python
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))

        return -sum(heap)
```
```python
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapify(pq)
        for _ in range(k): heapreplace(pq, pq[0]//2)
        return -sum(pq)
```

