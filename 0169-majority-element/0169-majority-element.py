class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for c in cnt:
            if cnt[c] > int(len(nums)//2):
                return c
        return -1