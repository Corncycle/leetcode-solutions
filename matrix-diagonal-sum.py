from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        out = 0
        n = len(mat)
        for i in range(n):
            out += mat[i][i] + mat[i][n-1-i]
        if n % 2 == 1:
            out -= mat[i // 2][i // 2]
        return out