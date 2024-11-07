class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        # n_idx = 0
        # # h_idx = 0
        # for i in range(len(haystack)):
        #     if haystack[i] == needle[n_idx]:
        #         n_idx += 1
        #         print(n_idx)
        #         if n_idx == len(needle):
        #             return i - len(needle) + 1
        #     else:
        #         n_idx = 0
        #         if haystack[i] == needle[n_idx]:
        #             n_idx += 1
        #             if n_idx == len(needle):
        #                 return i - len(needle) + 1
        # return -1