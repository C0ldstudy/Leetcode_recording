class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_index = sorted(range(len(nums)), key=nums.__getitem__)
        # print(num_index)
        flag = 0
        second = None
        for i in range(len(nums)):
            if not (i+1) in nums:
                second = i+1
            if flag == 0:
                if (nums[num_index[i]] == nums[num_index[i-1]]) :
                    first = nums[num_index[i]]
                    flag = 1
                    if second != None:
                        break
                elif i != (len(nums)-1):
                    if nums[num_index[i]] == nums[num_index[i+1]]:
                        first = nums[num_index[i]]
                        flag = 1    
                        if second != None:
                            break                        
        return [first, second]        

                
                
                
                # print(nums[nums[num_index[i]]-1], nums[num_index[i]], nums[num_index[i]])
#                 if nums[num_index[nums[num_index[i]]-1]] != nums[num_index[i]]:
#                     return [nums[num_index[nums[num_index[i]]-1]], first]
#                 else:
#                     return [nums[num_index[i]], first]
                    
#                 # break
        