class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        unique = []
        length = len(nums)
        while cnt < length:
            if nums[cnt] in unique:
                nums.pop(cnt)
                length -=1
            else:
                unique.append(nums[cnt])
                cnt += 1
        return length
                