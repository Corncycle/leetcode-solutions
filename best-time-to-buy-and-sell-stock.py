from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)
        mx = prices[-1]
        for i in reversed(range(len(prices)-1)):
            profits[i] = mx - prices[i]
            mx = max(mx, prices[i])
        return max(profits)