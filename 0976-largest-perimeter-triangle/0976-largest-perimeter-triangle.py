class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        else:
            sorted_nums = sorted(nums)
            # print(sorted_nums)
            for i in range(len(sorted_nums)-1, 1, -1):
                if sorted_nums[i] < sorted_nums[i-1] + sorted_nums[i-2]:
                    return sorted_nums[i] + sorted_nums[i-1] + sorted_nums[i-2]
                

            return 0
                
            