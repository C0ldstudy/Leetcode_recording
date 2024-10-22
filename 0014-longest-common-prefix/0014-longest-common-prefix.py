class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_str = strs[0]
        for s in strs:
            if len(s) < len(max_str):
                max_str = s
        prefix = ''
        for i in range(len(max_str)):
            for j in strs:
                if j[i] != max_str[i]:
                    return prefix
            prefix += max_str[i]
        return prefix
            