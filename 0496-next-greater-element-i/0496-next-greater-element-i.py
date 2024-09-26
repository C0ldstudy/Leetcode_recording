class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2 = nums2[::-1]
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    found = True
                elif found == True:
                    if nums1[i] < nums2[j]:
                        res[i] = nums2[j]
                        break
        return res
            
        