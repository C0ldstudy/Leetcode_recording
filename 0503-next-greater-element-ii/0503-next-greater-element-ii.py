class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        hashmap = [-1] * len(nums)
        
        for n in range(len(nums)):
            while stack and nums[n] > nums[stack[-1]]:
                hashmap[stack.pop(-1)] = nums[n]
            stack.append(n)
        # print(hashmap, stack)
        
        
        for n in range(len(nums)):
            while stack and nums[n] > nums[stack[-1]]:
                if hashmap[stack[-1]] == -1:
                    hashmap[stack.pop(-1)] = nums[n]
                else:
                    break
        
        return hashmap