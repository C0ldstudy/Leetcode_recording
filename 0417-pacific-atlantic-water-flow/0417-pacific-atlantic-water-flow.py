class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_queue = deque()
        atl_queue = deque()
        
        for i in range(rows):
            pac_queue.append((i,0))
            atl_queue.append((i, cols-1))
        for j in range(cols):
            pac_queue.append((0, j))
            atl_queue.append((rows-1, j))
            
        def bfs(queue):
            reachable = set()
            while queue:
                (row,col) = queue.popleft()
                reachable.add((row,col))
                adj = [(row+1, col), (row-1,col),(row,col+1),(row,col-1)]
                for new_row,new_col in adj:
                    if new_row<0 or new_row >=rows or new_col<0 or new_col >=cols:
                        continue
                    elif (new_row,new_col) in reachable:
                        continue
                    elif heights[new_row][new_col] < heights[row][col]:
                        continue
                    queue.append((new_row,new_col))
            return reachable
        
        pac_reachable = bfs(pac_queue)
        atl_reachable = bfs(atl_queue)
        return pac_reachable.intersection(atl_reachable)
            