class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest_streak = 0
        unique = set(nums)
        
        for start in nums:
            current_streak = 0
            current = start
            
            while current in unique:
                current_streak += 1
                
                if current * current > 10**5: break
                current *= current
                
            longest_streak = max(longest_streak, current_streak)
            
        return longest_streak if longest_streak >= 2 else -1