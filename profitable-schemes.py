from typing import List
from functools import lru_cache

# this recursive approach is given by the editorial for the problem
# https://leetcode.com/problems/profitable-schemes/editorial/
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(maxsize=None)
        def countWays(currProfit, currMembers, i):
            if i == len(profit):
                return 1 if currProfit == minProfit else 0
            numWays = countWays(currProfit, currMembers, i+1)
            if currMembers + group[i] <= n:
                numWays += countWays(min(minProfit, currProfit+profit[i]), currMembers + group[i], i+1)
            return numWays % 1_000_000_007

        return countWays(0, 0, 0)