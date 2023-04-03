from typing import List
from collections import deque

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s = deque(sorted(people))
        left, right = 0, len(s)-1
        count = 0
        while left < right:
            if s[left] + s[right] <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                right -= 1
        if left == right:
            count += 1
        return count