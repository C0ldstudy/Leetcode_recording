class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        update = True
        count = 0
        # old_update = 0
        while update:
            update = False
            adj = []
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 2:
                        adj += [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for i, j in adj:
                if (0<= i < rows) and (0<=j<cols):
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        update = True
            count += 1
            # print(grid)
        if any(1 in list for list in grid):
            return -1
        else:
            return count-1
        
                