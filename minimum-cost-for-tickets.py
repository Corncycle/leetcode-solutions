from typing import List
from functools import lru_cache

# here is my solution which is a very slow recursive approach
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days:
            return 0
        lengths = [1, 7, 30]
        totals = []
        for i in range(3):
            totals.append(costs[i]
                + self.mincostTickets([day for day in days if day >= days[0] + lengths[i]], costs))
        return min(totals)
'''

# this recursive solution is similar to the one above but allows caching
# it is due to the youtube channel "NeetCode": https://www.youtube.com/watch?v=4pY1bsBpIY4
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(i):
            if i == len(days):
                return 0
            totals = []
            for j, length in enumerate([1, 7, 30]):
                iend = i
                while iend < len(days) and days[iend] < days[i] + length:
                    iend += 1
                totals.append(costs[j] + helper(iend))
            return min(totals)
        return helper(0)