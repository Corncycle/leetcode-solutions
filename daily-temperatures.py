from typing import List
from collections import deque

# This monotonic stack approach is given by youtube channel NeetCode
# https://www.youtube.com/watch?v=cTBiBSnjO3c

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        out = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                out[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return out