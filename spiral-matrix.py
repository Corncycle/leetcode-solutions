from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        out = []

        for k in range(2 * min(n, m)):
            c = k // 4
            if k % 4 == 0:
                run = matrix[c][c:n-c]
            elif k % 4 == 1:
                run = [row[n-c-1] for row in matrix[c+1:m-c]]
            elif k % 4 == 2:
                run = reversed(matrix[m-c-1][c:n-c-1])
            else:
                run = reversed([row[c] for row in matrix[c+1:m-c-1]])
            out.extend(run)
        return out