class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: 
            return 0
        elif target > nums[-1]:
            return len(nums)
        
        left = 0
        right = len(nums)-1
        while left < right-1:
            middle = (left+right)//2
            if nums[middle]< target:
                left = middle
            elif nums[middle]> target:
                right = middle
            else:
                return middle
        if nums[left] < target:
            return right
        else:
            return left