### 790. Domino and Tromino Tiling
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.


### Solution
```python
class Solution:
    def numTilings(self, n: int) -> int:
# def numTilings(self, N):
        N = n
        A = [0] * (N + 1)
        B = [1, 1] + [0] * (N - 1)
        for i in range(2, N + 1):
            A[i] = (B[i - 2] + A[i - 1]) % int(1e9 + 7)
            B[i] = (B[i - 1] + B[i - 2] + A[i - 1] * 2) % int(1e9 + 7)
        return B[N]
```
