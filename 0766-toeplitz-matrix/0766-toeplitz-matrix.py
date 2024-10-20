class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        def check(row, col):
            base = matrix[row][col]            
            row += 1
            col += 1
            while (0<= row< rows) and (0<= col<cols):
                if matrix[row][col] != base:
                    return False
                row += 1
                col += 1
            return True
        for i in range(rows):
            if not check(i, 0):
                return False
        for j in range(1, cols):
            if not check(0, j):
                return False
        return True