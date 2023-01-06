from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs, i, remaining = sorted(costs), 0, coins
        while i < len(costs) and remaining >= costs[i]:
            remaining -= costs[i]
            i += 1
        return i