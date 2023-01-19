from typing import List
from collections import defaultdict
from itertools import accumulate

# This solution follows the reasoning in this video by NeetCode on youtube:
# https://www.youtube.com/watch?v=fFVZt-6sgyo
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        prefixes = defaultdict(int)

        for p in accumulate(nums):
            pmk = p % k
            total += prefixes[pmk]
            if pmk == 0:
                total += 1
            prefixes[pmk] += 1
        return total