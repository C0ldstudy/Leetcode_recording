class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        moves = [
            (2,1),
            (2,-1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),            
        ]
        def valid(to_row, to_col):
            if (0<=to_row<m) and (0<=to_col<n) and chessboard[to_row][to_col] == 0:
                return True
            else:
                return False
        def solve(c_row, c_col, move_count):
            if move_count == m*n:
                return True
            for move_r, move_c in moves:
                new_row, new_col = c_row+move_r, c_col+move_c
                if valid(new_row,new_col):
                    chessboard[new_row][new_col] = move_count
                    if solve(new_row, new_col, move_count+1):
                        return True
                    chessboard[new_row][new_col] = 0
            return False
        
        chessboard = [[0]*n for _ in range(m)]
        chessboard[r][c] = -1
        
        solve(r,c,1)
        chessboard[r][c] = 0
        return chessboard
            