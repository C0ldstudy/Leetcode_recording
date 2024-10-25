class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        cnt = 0
        while cnt < length:
            if nums[cnt] == val:
                nums.pop(cnt)
                length -=1
            else:
                cnt += 1
        return len(nums)