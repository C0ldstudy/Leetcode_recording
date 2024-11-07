class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        ori_color = image[sr][sc]
        
        while stack:
            row, col = stack.pop()
            adj = [(row, col),(row+1, col), (row-1, col), (row,col+1), (row, col-1)]
            for i,j in adj:
                if (0<=i<rows) and (0<=j<cols):
                    if image[i][j] == ori_color:
                        image[i][j] = color
                        stack.append((i,j))
        return image
                    
            