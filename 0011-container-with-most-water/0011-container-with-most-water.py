class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        sum_f = lambda i,j: min(height[i], height[j]) * (j-i)
        max_water = sum_f(left, right)
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            temp_sum = sum_f(left, right)
            max_water = max(max_water, temp_sum)
        return max_water
        