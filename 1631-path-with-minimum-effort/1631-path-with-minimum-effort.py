class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[math.inf]*cols for _ in range(rows)]
        efforts[0][0] = 0
        queue = [(0, 0,0)]
        visited = {(0,0)}
        while queue:
            diff, row,col = heapq.heappop(queue)
            adj = [(row+1, col), (row-1,col), (row, col+1), (row,col-1)]
            visited.add((row, col))
            for i,j in adj:
                if (0<=i<rows) and (0<=j<cols):
                    if (i,j) in visited: continue
                    temp = max(abs(heights[row][col] - heights[i][j]), efforts[row][col])
                    if efforts[i][j] > temp:
                        efforts[i][j] = temp
                        heapq.heappush(queue, (temp, i,j))
                    
        # print(efforts)
        return efforts[rows-1][cols-1]
                
                        
                    