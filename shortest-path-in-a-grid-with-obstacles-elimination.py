from typing import List

'''
    I had a go at this problem on my own, but my BFS approach was extremely 
    inefficient and I couldn't figure out how to optimize it on my own
    The approach here is due to the youtube channel "Algorithms Made Easy"
    https://www.youtube.com/watch?v=ID9YJXy3OJk
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        moves = 0
        endi = len(grid) - 1
        endj = len(grid[0]) - 1
        if k >= endi + endj:
            return endi + endj
        frontier = [(0, 0, k)]
        visited = set()
        while len(frontier) > 0:
            newFrontier = []
            for location in frontier:
                if location[0] == endi and location[1] == endj:
                    return moves
                visited.add(location)
                neighbors = [
                    (location[0] - 1, location[1]),
                    (location[0] + 1, location[1]),
                    (location[0], location[1] - 1),
                    (location[0], location[1] + 1),
                ]
                for i, j in neighbors:
                    if 0 <= i <= endi and 0 <= j <= endj:
                        if location[2] - grid[i][j] >= 0:
                            potential = (i, j) + (location[2] - grid[i][j],)
                            if potential not in newFrontier and potential not in visited:
                                newFrontier.append(potential)
            frontier = newFrontier
            moves += 1
        return -1