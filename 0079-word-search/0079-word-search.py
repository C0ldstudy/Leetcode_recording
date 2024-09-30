class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if rows * cols < len(word): return False
        counter = Counter(word)
        length = Counter(chain(*board))
        if counter > length: return False
        
        
        def dfs(i, j, s):
            if s==len(word): return True
            if (0 <= i < rows) and (0<=j<cols) and (word[s] == board[i][j]):
                tmp = board[i][j]
                board[i][j] = "#"
                adj = [(i-1, j), (i+1, j), (i,j+1), (i,j-1)]
                
                dp = any(dfs(ii, jj, s+1) for ii, jj in adj)
                board[i][j] = tmp
                return dp
            return False
        return any(dfs(i,j,0) for i,j in product(range(rows), range(cols)))
        
                