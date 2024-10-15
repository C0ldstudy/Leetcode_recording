class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for c in cnt:
            if cnt[c] == 1:
                return c
        return -1