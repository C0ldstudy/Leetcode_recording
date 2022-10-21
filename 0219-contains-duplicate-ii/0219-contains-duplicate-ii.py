class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # generate a dictionary to save the indexes with same values
        index_dict = {}
        for i, num in enumerate(nums):
            if not num in index_dict.keys():
                index_dict[num] = [i]
            else:
                index_dict[num].append(i)
        #check each item meeting abs(i-j) <=k
        for key,value in index_dict.items():
            if len(value) >=2:
                # value = abs(value)
                for i in range(len(value)-1):   
                    if abs(value[i+1]-value[i])<=k:
                        return True
        return False
        