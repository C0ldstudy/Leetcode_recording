### 931. Minimum Falling Path Sum
Given an `n x n` array of integers `matrix`, return the **minimum sum of any falling path** through `matrix`.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

### Key idea
- Dynamic programming


### Solution
The first thing in my mind is a greedy algorithm. But after evaluation I found that greedy algorithm does not work. DP is necessary.
```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        result = min(matrix[0])
        index = [matrix[0].index(result)]
        print(result)
        def update(index):
            updated_index = []
            for i in index:
                updated_index += [i-1,i,i+1]
            updated_index = [i for i in updated_index if ((i>=0) and (i<len(matrix))) ]
            return updated_index

        for i in range(1, len(matrix)):
            candidate_index = update(index)

            temp = [matrix[i][j] for j in candidate_index]

            row_result = min(temp)
            print(row_result)
            result += row_result
            index = [matrix[i].index(row_result)]
        return result
```

Dynamic Proramming
```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        @cache
        def go(i, j):
            if j < 0 or j == N:
                return float('inf')
            if not i:
                return matrix[i][j]
            a = go(i - 1, j - 1)
            b = go(i - 1, j)
            c = go(i - 1, j + 1)
            return matrix[i][j] + min(a, b, c)
        best = float('inf')
        for j in range(N):
            best = min(best, go(M - 1, j))
        return best
```
The bottom-up solution
```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        for i in range(1, M):
            for j in range(N):
                a = matrix[i - 1][j - 1] if 0 <= j - 1 else float('inf')
                b = matrix[i - 1][j]
                c = matrix[i - 1][j + 1] if j + 1 < N else float('inf')
                matrix[i][j] += min(a, b, c)
        return min(matrix[M - 1])
```



