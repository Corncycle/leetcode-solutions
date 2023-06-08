from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        out = 0
        n = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    out += n - j
                    break

        return out