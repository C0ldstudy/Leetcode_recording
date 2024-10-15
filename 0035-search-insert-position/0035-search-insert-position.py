class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: 
            return 0
        elif target > nums[-1]:
            return len(nums)
        
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if nums[middle]< target:
                left = middle + 1
            elif nums[middle]> target:
                right = middle-1
            else:
                return middle
        return left
