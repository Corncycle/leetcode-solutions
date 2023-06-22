from typing import List

# This approach is due to the editorial for the problem
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/editorial/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = [0 for _ in prices]
        free = [0 for _ in prices]

        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], free[i-1] - prices[i])
            free[i] = max(free[i-1], hold[i-1] + prices[i] - fee)

        return free[-1]