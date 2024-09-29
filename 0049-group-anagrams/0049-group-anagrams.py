class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if not key in dic.keys():        
                dic[key] = [] # set()
            dic[key].append(s) #.add(s)
        res = []
        for k in dic:
            res.append(list(dic[k]))
        return res
        
            
        