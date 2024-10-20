class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        for i in range(k):
            temp = -heapq.heappop(max_heap)
            score += temp
            heapq.heappush(max_heap, -ceil(temp/3))
        return score
        