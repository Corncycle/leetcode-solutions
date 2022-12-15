'''This approach for this solution is due to Timothy H Chang on Youtube:
https://www.youtube.com/watch?v=lJxoNrJL3kU
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = list(text1)
        t2 = list(text2)

        dp = [[0 for _ in range(len(t2) + 1)] for _ in range(len(t1) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if t1[i - 1] == t2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]