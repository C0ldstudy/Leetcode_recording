class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2+1)
        label = 1
        cols = list(range(0, n))
        for row in range(n-1, -1, -1):
            for col in cols:
                cells[label] = (row, col)
                label += 1
            cols.reverse()
        dist = [-1] * (n**2 + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for next in range(curr+1, min(curr+6, n**2)+1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1 else next)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        return dist[n*n]
            