The essence of the problem is to combine the largest two numbers together and iteratively check the smallest number. If it meets the trainage requirements (the sum of two samller sides are larger than the third side), we return the perimeter.
​
```python
class Solution:
def largestPerimeter(self, nums: List[int]) -> int:
if len(nums) < 3:
return 0
else:
sorted_nums = sorted(nums)
sorted_nums.reverse()
for i in range(len(sorted_nums)-2):
number1 = sorted_nums[i]
number2 = sorted_nums[i+1]
for j in range(i+2, len(sorted_nums)):
number3 = sorted_nums[j]
if number3+number2>number1:
return number3+number2+number1
return 0
```
​
A better way:
If the continuous three numbers do not meet the triangle sides requirement, then it cannot meet! Do not need to check the smaller items.