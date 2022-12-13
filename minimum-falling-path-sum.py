from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        running = matrix[-1]
        print(running)
        for i in range(len(matrix) - 2, -1, -1):
            running = self.combineRows(running, matrix[i])
            print(running)
        return min(running)

    def combineRows(self, running: List[int], row: List[int]) -> int:
        newRunning = []
        for j, val in enumerate(row):
            candidates = [val + running[j + jj] for jj in [-1, 0, 1] if 0 <= j + jj < len(row)]
            newRunning.append(min(candidates))
        return newRunning