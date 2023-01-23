from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        degrees = {i: 0 for i in range(1, n + 1)}
        for s, d in trust:
            degrees[s] -= 1
            degrees[d] += 1
        candidates = [person for person in degrees if degrees[person] == n - 1]
        return candidates[0] if len(candidates) == 1 else -1