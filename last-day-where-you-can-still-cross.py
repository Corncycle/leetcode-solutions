from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0 for _ in range(col)] for __ in range(row)]

        def editGrid(currDay, goalDay):
            if currDay < goalDay:
                for day in range(currDay, goalDay):
                    grid[cells[day][0]-1][cells[day][1]-1] = 1
            else:
                for day in reversed(range(goalDay, currDay + 1)):
                    grid[cells[day][0]-1][cells[day][1]-1] = 0
                
        def getCrossability():
            frontier = deque()
            visited = set()

            for startj in range(col):
                if grid[0][startj] == 0:
                    frontier.append((0, startj))
                    visited.add((0, startj))
            while frontier:
                i, j = frontier.popleft()
                if i == row - 1:
                    return True
                for ii, jj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= i + ii < row and 0 <= j + jj < col:
                        if (i + ii, j + jj) not in visited and grid[i + ii][j + jj] == 0:
                            frontier.append((i + ii, j + jj))
                            visited.add((i + ii, j + jj))
            return False
        
        left, right = 0, row * col
        lastWasCrossable = True # "last" being 0 water tiles to begin with
        while left < right - 1:
            next = (left + right) // 2
            if lastWasCrossable:
                editGrid(left, next)
            else:
                editGrid(right, next)
            if getCrossability():
                left = next
                lastWasCrossable = True
            else:
                right = next
                lastWasCrossable = False
        return left