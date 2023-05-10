from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[0 for i in range(n)] for j in range(n)]

        curr = 1
        for k in range(2 * n - 1):
            c = k // 4
            if k % 4 == 0:
                for j in range(c, n-c):
                    out[c][j] = curr
                    curr += 1
            elif k % 4 == 1:
                for i in range(c+1, n-c):
                    out[i][n-c-1] = curr
                    curr += 1
            elif k % 4 == 2:
                for j in reversed(range(c, n-c-1)):
                    out[n-c-1][j] = curr
                    curr += 1
            else:
                for i in reversed(range(c+1, n-c-1)):
                    out[i][c] = curr
                    curr +=1

        return out