class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_c = -1
        for c in cnt:
            if (cnt[c] == 1) and (max_c < c):
                max_c = c
        return max_c