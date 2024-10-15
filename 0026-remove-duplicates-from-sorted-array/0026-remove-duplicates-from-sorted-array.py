class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        idx = 0
        length = len(nums)
        while idx < length:
            if nums[idx] not in stack:
                stack.append(nums[idx])
                idx += 1
            else:
                nums.pop(idx)
                length -= 1
        return len(nums)