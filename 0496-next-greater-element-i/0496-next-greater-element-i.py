class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        for idx1 in range(len(nums1)):
            found = False
            for n2 in nums2:
                if n2 == nums1[idx1]:
                    found = True
                elif found and n2 > nums1[idx1]:
                    result[idx1] = n2
                    break
        return result