from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def populateIsland(i0, j0):
            frontier = [(i0, j0)]
            visited = {(i0, j0)}
            isClosed = True
            while frontier:
                i, j = frontier.pop()
                grid[i][j] = 2
                for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i + ii < height and 0 <= j + jj < width:
                        if grid[i+ii][j+jj] == 0 and (i+ii, j+jj) not in visited:
                            visited.add((i+ii, j+jj))
                            frontier.append((i+ii, j+jj))
                    else:
                        isClosed = False
            return 1 if isClosed else 0

        height, width = len(grid), len(grid[0])
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    count += populateIsland(i, j)
        return count