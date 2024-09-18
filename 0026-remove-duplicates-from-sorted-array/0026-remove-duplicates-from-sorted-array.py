class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in nums[1:]:
            # print(count, i, nums)
            if nums[count] != i:
                count += 1
            else:
                nums.pop(count)
            
        return count+1
            
            
            
        