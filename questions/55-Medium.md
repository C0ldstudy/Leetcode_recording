### 55. Jump Game
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Key idea
- No need to record the different ways to reach a point. Just yes or not is enough.
- Just need to record the maximal range.

### Solution
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        answer = [None for _ in range(length)]
        answer[0] = True
        cur = 0
        for i in range(length):
            if answer[i] != True: continue
            else:
                item_range = nums[i]

                for j in range(cur,(i+item_range+1)):
                    answer[j] = True
                    if j == (length - 1): return answer[j]
                cur = i+item_range

            # print(answer)
        return answer[-1]
```
Omit answer array:
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        cur = 0
        for i in range(length):
            if cur < i: return False
            else:
                item_range = nums[i]
                cur = max(i+item_range, cur)
                if cur >= (length - 1): return True
        return False
```
