class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: return []
        dic = {}
        rank = 1
        s_arr = sorted(arr)
        dic[s_arr[0]] = 1
        for i in range(1, len(arr)):            
            if s_arr[i] > s_arr[i-1]:
                rank += 1
                dic[s_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr
            

            
        
