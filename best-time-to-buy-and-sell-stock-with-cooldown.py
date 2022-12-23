from typing import List
from collections import defaultdict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = -5000 * 1000
        # state[i][j]: highest amt that can be had on day i while holding j stocks
        states = [defaultdict(lambda: lowest) for _ in range(len(prices) + 1)]
        states[0][0] = 0

        def processStates(i):
            for state in states[i]:
                states[i+1][state] = max(states[i+1][state], states[i][state])
                if state == 0:
                    states[i+1][state+1] = max(states[i+1][state+1], states[i][state] - prices[i])
                else:
                    if i < len(prices) - 1:
                        states[i+2][state-1] = max(states[i+2][state-1], states[i][state] + prices[i])
                    else:
                        states[i+1][state-1] = max(states[i+1][state-1], states[i][state] + prices[i])

        for i in range(len(prices)):
            processStates(i)

        return max(states[-1][state] for state in states[-1])