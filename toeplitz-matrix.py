from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            start = matrix[i][0]
            for j in range(1, min(m - i, n)):
                if matrix[i + j][j] != start:
                    return False

        for j in range(n):
            start = matrix[0][j]
            for i in range(1, min(m, n - j)):
                if matrix[i][i + j] != start:
                    return False

        return True