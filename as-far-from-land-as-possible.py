from typing import List

# pretty standard bfs
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])
        known = {}
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    known[(j, i)] = 0
        if len(known) == 0 or len(known) == height * width:
            return -1
        
        def neighbors(coords):
            out = []
            for offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                candidate = (coords[0] + offset[0], coords[1] + offset[1])
                if 0 <= candidate[0] < width and 0 <= candidate[1] < height:
                    out.append(candidate)
            return out
        
        frontier = set(known)
        newFrontier = set()
        dist = 1
        while True:
            for loc in frontier:
                for neigh in neighbors(loc):
                    if neigh not in known:
                        known[neigh] = dist
                        newFrontier.add(neigh)
            if newFrontier:
                frontier = newFrontier
                newFrontier = set()
                dist += 1
            else:
                return dist - 1