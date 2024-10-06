class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        left = max(0, left)
        right = min(len(self.data), right)
        for i in range(left, right+1):
            sum += self.data[i]
        return sum
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)