### 739. Daily Temperatures

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i^th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.


### Key idea
- One thing I learned is the importance of the data structure. It is a trade-off between space complexity and time complexity.




### Solution
My original solution meet the time limit exceeded problem.
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        if length == 1: return [0]
        result = [0]

        for i in range(length-2, -1, -1):
            cur = temperatures[i]
            for j in range(i+1, length):
                if temperatures[j] > cur:
                    result.insert(0, j-i)
                    break
                if j == length-1:
                    result.insert(0, 0)
                    break
        return result
```

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        length = len(temperatures)
        if length == 1: return [0]

        arr = [-1 for _ in range(71)]
        res = [0] * length

        for i in range(length-1,-1,-1):
            t = temperatures[i]
            j = [x for x in arr[t-30+1:] if x > -1]
            res[i] = 0 if len(j) == 0 else min(j)-i
            arr[t-30] = i

        return res
```
Use Stack: https://leetcode.com/problems/daily-temperatures/solutions/109820/simple-python-o-n-using-stack/

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if len(temperatures) <= 1:
            return [0]
        stack = [len(temperatures)-1]
        ans = [0]
        for pos in range(len(temperatures)-2, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[pos]:
                stack.pop()
            if len(stack) == 0:
                ans.append(0)
            else:
                ans.append(stack[-1]-pos)
            stack.append(pos)
        ans.reverse()
        return ans
```

