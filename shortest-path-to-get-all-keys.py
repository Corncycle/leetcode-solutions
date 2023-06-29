from typing import List
from collections import deque

def hasKey(keys, c):
    temp = keys
    for _ in range(ord(c) - ord("a")):
        temp = temp // 2
    return (temp % 2) > 0

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        frontier = deque()
        visited = set()
        m, n = len(grid), len(grid[0])

        allKeys = 0 # encode keys in the grid in a bitmask
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in "abcdef":
                    allKeys += 2 ** (ord(grid[i][j]) - ord("a"))
                elif grid[i][j] == "@":
                    starti, startj = i, j

        # frontier states: (i, j, keysMask, numSteps)
        frontier.append((starti, startj, 0, 0))
        visited.add((starti, startj, 0))

        while frontier:
            i, j, keysMask, numSteps = frontier.popleft()
            if keysMask == allKeys:
                return numSteps
            for ii, jj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= i + ii < m and 0 <= j + jj < n and grid[i + ii][j + jj] != "#":
                    newMask = keysMask
                    if grid[i + ii][j + jj] in "ABCDEF":
                        if not hasKey(keysMask, grid[i + ii][j + jj].lower()):
                            continue
                    elif grid[i + ii][j + jj] in "abcdef":
                        if not hasKey(keysMask, grid[i + ii][j + jj].lower()):
                            newMask += 2 ** (ord(grid[i + ii][j + jj]) - ord("a"))
                    if (i + ii, j + jj, newMask) in visited:
                        continue
                    frontier.append((i + ii, j + jj, newMask, numSteps + 1))
                    visited.add((i + ii, j + jj, newMask))
        return -1