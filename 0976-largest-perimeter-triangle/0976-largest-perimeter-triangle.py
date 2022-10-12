class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        else:
            sorted_nums = sorted(nums)
            sorted_nums.reverse()
            for i in range(len(sorted_nums)-2):
                number1 = sorted_nums[i]
                number2 = sorted_nums[i+1]
                for j in range(i+2, len(sorted_nums)):
                    number3 = sorted_nums[j]
                    # print(number3, number2, number1)
                    if number3+number2>number1:
                        return number3+number2+number1
            return 0
                
            