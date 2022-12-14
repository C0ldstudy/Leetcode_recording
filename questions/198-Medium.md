### 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night.**

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


### Key idea
- get the local optimal result one by one


### Solution
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2: return nums[0]
        best_result = [None]*length
        # print(best_result)
        def dp(index):
            if index == 0:
                return nums[index]
            elif index == 1:
                return max(nums[0], nums[1])
            result = max(best_result[index-2]+nums[index], best_result[index-1])
            return result
        for i in range(length):
            print(i)
            best_result[i] = dp(i)
        return best_result[-1]
```
