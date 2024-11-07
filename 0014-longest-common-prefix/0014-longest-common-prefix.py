class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = strs[0]
        for s in strs:
            if len(s) < len(min_str):
                min_str = s
        com = ""
        for i in range(len(min_str)):
            for j in range(len(strs)):
                if strs[j][i] != min_str[i]:
                    return com
            com += min_str[i]
        return com
