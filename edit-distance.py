from functools import lru_cache

# this solution is due to Timothy H Chang from the following video:
# https://www.youtube.com/watch?v=jkwSsFAPVUk

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # i points at an index of word1, j points at an index of word2
        @lru_cache(None)
        def helper(i, j):
            if i >= n and j >= m:
                return 0
            elif i >= n:
                return m - j
            elif j >= m:
                return n - i
            
            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            else:
                replace = 1 + helper(i+1, j+1)
                delete = 1 + helper(i+1, j)
                insert = 1 + helper(i, j+1)
                return min(replace, delete, insert)
        
        return helper(0, 0)