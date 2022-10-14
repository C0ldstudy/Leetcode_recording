class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        else:
            nums_index = sorted(range(len(nums)),key=nums.__getitem__)
            left = 0
            right = len(nums)-1
            # print(left, right)
            while nums[nums_index[left]] + nums[nums_index[right]] != target:
                if nums[nums_index[left]] + nums[nums_index[right]] > target:
                    right -= 1
                else:
                    left += 1
                # print(left, right)
            return [nums_index[left], nums_index[right]]
            
    
    

        
        