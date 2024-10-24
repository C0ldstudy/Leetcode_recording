class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        
        for n2 in nums2:
            while stack and n2 > stack[-1]:
                hashmap[stack.pop(-1)] = n2
            stack.append(n2)
        
        while stack:
            hashmap[stack.pop()] = -1
            
        
        # print(hashmap)
        return [hashmap.get(i, -1) for i in nums1]