class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        result = [False] * len(candies)
        for idx in range(len(candies)):
            if candies[idx] + extraCandies >= max_c:
                result[idx] = True
        return result