class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid)-1
        max_col = len(grid[0])-1
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
            
            
        queue = deque([(0,0,1)])
        visited = {(0,0)}
        while queue:
            # print(visited, queue)
            row, col, dis = queue.popleft()
            if (row, col) == (max_row, max_col):
                return dis
            adj = [(row+1, col), (row-1, col), (row+1, col+1), (row-1, col-1), (row, col-1), (row, col+1), (row+1,  col-1), (row-1, col+1)]
            for (i,j) in adj:
                if (0<=i<=max_row) and (0<=j<=max_col):
                    if grid[i][j] != 0: continue
                    if (i,j) in visited: continue
                    visited.add((i,j))
                    queue.append((i,j, dis+1))
            
                    
        return -1