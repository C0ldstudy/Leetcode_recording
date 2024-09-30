class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        dp = [0] * len(nums)
        bond = len(nums)-1
        dp[0] = nums[0]
        max_bond = nums[0]
        for i in range(1, len(nums)):
            if max_bond < i: return False
            dp[i] = max(dp[i-1], i + nums[i])
            max_bond = max(dp[i], max_bond)
            if dp[i] >= bond: return True
        # print(dp)
        return False
            
            
        