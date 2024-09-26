class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return self.check(coordinate1[0], coordinate1[1]) == self.check(coordinate2[0], coordinate2[1])
        
        
        
    def check(self, c1, c2):
        if ord(c1) % 2 == 0:
            if int(c2) % 2 == 0:
                return 1
            else:
                return 0
        else:
            if int(c2) % 2 == 0:
                return 0
            else:
                return 1            