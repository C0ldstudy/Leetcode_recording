class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()
        for i in range(len(arr1)):
            while not (arr1[i] in prefix) and arr1[i] > 0:
                prefix.add(arr1[i])
                arr1[i] //= 10
        longest = 0
        for i in range(len(arr2)):
            while not (arr2[i] in prefix) and arr2[i] > 0:
                arr2[i] //= 10
            if arr2[i] > 0:
                longest = max(longest, len(str(arr2[i])))
        return longest
    
