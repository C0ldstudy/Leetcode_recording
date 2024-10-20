class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: return []
        dic = {}
        rank = 1
        for n in sorted(arr):
            if n not in dic:
                dic[n] = rank
                rank += 1
        # print(dic)
        result = []
        for n in arr:
            result.append(dic[n])
        return result
            