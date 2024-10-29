class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis = [[False] * cols for _ in range(rows)]
        stack = []
        max_depth = 0
        for i in range(rows):
            stack.append((i,0,0))
            vis[i][0] = True
        
        while stack:
            row, col, depth = stack.pop()
            adj = [(row-1, col+1), (row, col+1), (row+1, col+1)]
            for ii,jj in adj:
                if (0<= ii < rows) and (0<=jj<cols) and (vis[ii][jj]==False) and(grid[ii][jj] > grid[row][col]):
                    vis[ii][jj] = True
                    stack.append((ii,jj,depth+1))
                    max_depth = max(max_depth, depth+1)
        return max_depth
                
                    
            