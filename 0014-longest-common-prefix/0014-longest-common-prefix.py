class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = min(strs, key=len)
        common = ""  
        flag = 0
        for i in range(len(w)):
            for j in range(len(strs)):
                if w[i] != strs[j][i]:
                    flag = 1
                    break
            if flag == 0:
                common += w[i]
            elif flag == 1:
                return common
        return common
            
        