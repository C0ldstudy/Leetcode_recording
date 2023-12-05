Not efficient method: (O^2):
```
class Solution:
def maxArea(self, height: List[int]) -> int:
max_water = 0
for i in range(len(height)):
for j in range(1, len(height)):
temp_sum = min(height[i], height[j]) * (j-i)
max_water = max(max_water, temp_sum)
return max_water
```