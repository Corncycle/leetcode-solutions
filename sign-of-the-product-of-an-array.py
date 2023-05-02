from typing import List
from math import prod

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def sign(n):
            return 1 if n > 0 else (-1 if n < 0 else 0)
        return prod(sign(n) for n in nums)