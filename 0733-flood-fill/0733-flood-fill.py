class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image),len(image[0])
        original_color = image[sr][sc]
        if image[sr][sc] == color: return image
        image[sr][sc] = color
        def dfs(i,j,image):
            if (0<= i < rows) and (0<= j < cols):
                
                adj = [(i+1, j), (i-1, j), (i, j+1), (i,j-1)]
                for ii, jj in adj:
                    if (0<= ii < rows) and (0<= jj < cols):
                        if image[ii][jj] == original_color:
                            image[ii][jj] = color
                            # res.append([ii,jj])
                            dfs(ii, jj, image)
        dfs(sr, sc, image)

        return image