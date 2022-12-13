### 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



### Solutions:
```python
# Actually the result is Fibonacci number
# So the easiest way is to just output Fibonacci number
# My solution is to sum up each type number of the 2
class Solution:
    def climbStairs(self, n: int) -> int:
        types = int(n/2)
        result = 1
        for i in range(1, types+1):
            if i == 1: result += n-1
            else:
                left = n - i*2
                result += math.comb(left+i,i)
            # print(result)
        return result
```
