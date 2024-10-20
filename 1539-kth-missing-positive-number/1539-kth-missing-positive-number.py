class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 1
        while True:
            if cnt not in arr:
                k -=1
                if k == 0:
                    return cnt
            cnt += 1                
                