class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = float('inf')
        second = float('inf')
        for i, number in enumerate(nums):
            if number <= first:
                first = number
            elif number <= second:
                second = number
            elif number > second:
                return True
            # print(first, second)
        return False
            