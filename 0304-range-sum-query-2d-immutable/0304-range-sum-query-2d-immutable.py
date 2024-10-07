class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.data = [[0]* (col+1)  for _ in range(row+1)]
        self.data[row-1][col-1] = matrix[row-1][col-1]
        for i in range(col-2, -1, -1):
            self.data[row-1][i] = self.data[row-1][i+1] + matrix[row-1][i]
        for j in range(row-2, -1, -1):
            self.data[j][col-1] = self.data[j+1][col-1] + matrix[j][col-1]
            
        for i in range(row-2, -1, -1):
            for j in range(col-2, -1, -1):
                self.data[i][j] = self.data[i+1][j] + self.data[i][j+1]-self.data[i+1][j+1] + matrix[i][j]
        
                
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.data[row1][col1]+self.data[row2+1][col2+1]-self.data[row2+1][col1]-self.data[row1][col2+1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)