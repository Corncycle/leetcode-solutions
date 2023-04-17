from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        out = []
        for kid in candies:
            out.append(kid + extraCandies >= m)
        return out
