class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        result = []
        for n1 in nums1:
            # print(n1, result)
            if len(nums2) == 0: return result
            if n1 in nums2:
                result.append(n1)
                for i in range(len(nums2)):
                    if n1 == nums2[i]:
                        nums2.pop(i)
                        break
        return result
                
                        
            