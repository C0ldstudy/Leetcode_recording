class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        res = [1] * numRows
                
        
        previous_rows = self.generate(numRows-1)
        pre_row = previous_rows[-1]
        
        for i in range(1, numRows-1):
            res[i] = (pre_row[i-1] + pre_row[i])
            
        previous_rows.append(res)
        return previous_rows
            