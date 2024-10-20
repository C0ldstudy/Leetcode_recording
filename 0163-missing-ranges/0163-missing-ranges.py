class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
            
        result = []
        if lower < nums[0]:
            result.append([lower, nums[0]-1])
            # nums = [lower] + nums

        
        for idx in range(len(nums)-1):
            if nums[idx]+1 < nums[idx+1]:
                result.append([nums[idx]+1, nums[idx+1]-1])
        if upper > nums[-1]:
            result.append([nums[-1]+1, upper])
            # nums.append(upper)
            
        return result
            