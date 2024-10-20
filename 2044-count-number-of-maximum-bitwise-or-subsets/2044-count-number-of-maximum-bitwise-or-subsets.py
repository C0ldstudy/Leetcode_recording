class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        return self.count(nums, 0, 0, max_or_value)
    
    def count(self, nums, index, current_or, target_or):
        if index == len(nums):
            return 1 if current_or == target_or else 0
        count_without = self.count(nums, index+1, current_or, target_or)
        count_with = self.count(nums, index+1, current_or | nums[index], target_or)
        return count_without+count_with