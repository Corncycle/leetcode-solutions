from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.numTiles = 0
        
        def populate(i0, j0):
            frontier = [(i0, j0)]
            visited = {(i0, j0)}
            isOnBoundary = False
            while frontier:
                i, j = frontier.pop()
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    isOnBoundary = True
                for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i+ii < m and 0 <= j+jj < n:
                        if grid[i+ii][j+jj] == 1 and (i+ii, j+jj) not in visited:
                            frontier.append((i+ii, j+jj))
                            visited.add((i+ii, j+jj))
                            grid[i+ii][j+jj] = 2
            if not isOnBoundary:
                self.numTiles += len(visited)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    populate(i, j)

        return self.numTiles