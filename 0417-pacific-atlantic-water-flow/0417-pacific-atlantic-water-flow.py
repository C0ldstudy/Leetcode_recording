class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n-1))
        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m-1, i))
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                for (x,y) in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_row, new_col = row +x, col+y
                    if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                        continue
                    if (new_row,new_col) in reachable:
                        continue
                    if heights[new_row][new_col]< heights[row][col]:
                        continue
                    queue.append((new_row, new_col))
            return reachable
        
        pracific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        return list(pracific_reachable.intersection(atlantic_reachable))
                        