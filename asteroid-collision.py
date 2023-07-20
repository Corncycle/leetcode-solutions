from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        d = deque()
        for a in asteroids:
            if a < 0:
                while d and d[-1] > 0 and -a > d[-1]:
                    d.pop()
                if d and a + d[-1] == 0:
                    d.pop()
                elif (d and d[-1] < 0) or not d:
                    d.append(a)
            else:
                d.append(a)
        return list(d)