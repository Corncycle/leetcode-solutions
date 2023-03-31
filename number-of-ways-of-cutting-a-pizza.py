from typing import List

# this dynamic programming approach is given by the editorial for this problem:
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/editorial/
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        dp = [[[0 for _ in range(k)] for col in pizza[0]] for row in pizza]
        apples = [[0 for _ in range(cols+1)] for __ in range(rows+1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                apples[i][j] = ((1 if pizza[i][j] == "A" else 0)
                    + apples[i+1][j]
                    + apples[i][j+1]
                    - apples[i+1][j+1])
                if apples[i][j] > 0:
                    dp[i][j][0] = 1

        for cuts in range(1, k):
            for i in range(rows):
                for j in range(cols):
                    numWays = 0
                    for ii in range(i+1, rows):
                        if apples[ii][j] < apples[i][j]:
                            numWays += dp[ii][j][cuts-1]
                    for jj in range(j+1, cols):
                        if apples[i][jj] < apples[i][j]:
                            numWays += dp[i][jj][cuts-1]
                    dp[i][j][cuts] = numWays % 1_000_000_007

        return dp[0][0][k-1]