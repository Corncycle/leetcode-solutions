from typing import List
import functools

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        maxI = len(grid) - 1
        maxJ = len(grid[0]) - 1
        
        numSquares = 0
        start = (-1, -1)
        for i in range(maxI + 1):
            for j in range(maxJ + 1):
                if grid[i][j] >= 0:
                    numSquares += 1
                if grid[i][j] == 1:
                    start = (i, j)

        def getNeighbors(loc):
            i, j = loc
            out = []
            out.append((i - 1, j)) if i > 0 else None
            out.append((i + 1, j)) if i < maxI else None
            out.append((i, j - 1)) if j > 0 else None
            out.append((i, j + 1)) if j < maxJ else None
            return out

        @functools.lru_cache(maxsize=None)
        def getPaths(visited, last):
            if grid[last[0]][last[1]] == 2:
                return 1 if len(visited) == numSquares else 0
            neighbors = getNeighbors(last)
            neighbors = [neigh for neigh in neighbors if neigh not in visited and grid[neigh[0]][neigh[1]] >= 0]
            out = 0
            for neigh in neighbors:
                out += getPaths(visited | {neigh}, neigh)
            return out

        return getPaths(frozenset({start}), start)

s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
