class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0
        for i in nums:
            if i == 0:
                max_count = max(max_count, curr_count)
                curr_count = 0
            if i == 1:
                curr_count += 1
        max_count = max(max_count, curr_count)                
        return max_count
            