class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boundary = max(candies)-extraCandies
        res = [False] * len(candies)
        for i, c in enumerate(candies):
            if c >= boundary:
                res[i] = True
        return res