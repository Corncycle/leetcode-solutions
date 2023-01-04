from typing import List
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        grouped = Counter(tasks)
        out = 0
        for count in grouped.values():
            if count == 1:
                return -1
            else:
                numTwos = -count % 3
                out += numTwos
                out += (count - 2 * numTwos) // 3
        return out