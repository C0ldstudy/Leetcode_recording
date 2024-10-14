class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        com = ''
        for i in range(len(base)):
            for j in range(1, len(strs)):
                if (len(strs[j])-1) < i: return com
                if strs[j][i] != base[i]:
                    return com
            com += base[i]
        return com
                
            
            