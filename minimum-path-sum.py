from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cumulative = [[0 for j in range(n)] for i in range(m)]
        cumulative[m-1][n-1] = grid[m-1][n-1]
        for j in reversed(range(n-1)):
            cumulative[m-1][j] = grid[m-1][j] + cumulative[m-1][j+1]
        for i in reversed(range(m-1)):
            cumulative[i][n-1] = grid[i][n-1] + cumulative[i+1][n-1]
            for j in reversed(range(n-1)):
                cumulative[i][j] = grid[i][j] + min(cumulative[i+1][j], cumulative[i][j+1])
        return cumulative[0][0]