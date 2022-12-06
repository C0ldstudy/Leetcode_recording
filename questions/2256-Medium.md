### 2256. Minimum Average Difference




This is my first trial but it failed if nums is a super large array.
```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1: return 0
        pre = [nums[0]]
        post = [0]
        for i in range(1, length):
            pre.append((pre[i-1]*i+nums[i])/(i+1))
            post.insert(0, (post[-i]*(i-1)+nums[length-i])/i)
        # print(pre, post)
        min_index = 0
        min_value = float(inf)
        for i in range(length):
            if abs(int(pre[i])-int(post[i]))<min_value:
                # print(abs(int(pre[i])-int(post[i])), min_value)
                min_index = i
                min_value = abs(int(pre[i])-int(post[i]))
        return min_index
```
The way I tried is called `Prefix Sum`. Basically, `Prefix Sum` used two arrays to save the sum once and add or substract based on the previous results.

I found an optimized method here in the same direction. The key difference is not to store the middle results and just keep the minimal value and index.
```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l, r, n, md, mi = 0, sum(nums), len(nums), float('inf'), None
        for i, x in enumerate(nums):
            l, r = l + x, r - x
            d = abs((l // (i + 1)) - ((r // (n - i - 1)) if r else 0))
            if d < md:
                mi, md = i, d
        return mi
```

