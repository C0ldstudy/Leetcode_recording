class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        length = len(nums)
        while cnt < length:
            if nums[cnt] == 0:
                nums.pop(cnt)
                nums.append(0)
                length -= 1
            else:
                cnt += 1
                
        return        