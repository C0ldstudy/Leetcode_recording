class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x: str(x)*10, reverse = True)
        if nums[0] == 0: return "0"
        # print(nums)
        result = ""
        for i in nums:
            result += str(i)
        return result