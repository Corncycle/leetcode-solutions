from functools import lru_cache

# this recursive approach is due to the editorial for this problem:
# https://leetcode.com/problems/longest-palindromic-subsequence/editorial/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # `start` and `end` both inclusive
        @lru_cache(maxsize=None)
        def helper(start, end):
            if end - start == 1:
                return 2 if s[end] == s[start] else 1
            elif end - start == 0:
                return 1
            if s[end] == s[start]:
                return 2 + helper(start + 1, end - 1)
            else:
                return max(helper(start + 1, end), helper(start, end - 1))

        return helper(0, len(s) - 1)