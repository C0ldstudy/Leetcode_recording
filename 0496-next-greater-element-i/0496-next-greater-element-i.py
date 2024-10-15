class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] *len(nums1)
        for idx, n1 in enumerate(nums1):
            found = False
            for n2 in nums2:
                if n2 == n1: found = True
                if (found == True) and (n2 > n1):
                    result[idx] = n2
                    break
        return result
                    
                    