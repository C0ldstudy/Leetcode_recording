class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = "0"*(32-len(s))+s
        s = s[::-1]
        
        s = int(s, 2)
        
        # print(s)
        return s
        
        