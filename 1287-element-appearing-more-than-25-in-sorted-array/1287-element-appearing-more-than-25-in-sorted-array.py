class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = int(len(arr)/4)
        # print(length)
        i = 0 # do not need to compare with itself
        n = arr[i]
        c = 0        
        while i < len(arr):
            # print(i, arr[i], n, c)
            if arr[i] == n:
                c += 1
                if c > length:
                    return n
            else:
                n = arr[i]
                c = 1
            if i < len(arr):
                i += 1
        return n
                

            
        