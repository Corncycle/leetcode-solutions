from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacityWorks(cap):
            curr = 0
            count = 1
            for weight in weights:
                if weight + curr > cap:
                    count += 1
                    curr = weight
                else:
                    curr += weight
                if count > days:
                    return False
            return True
        
        left = max(weights)
        right = sum(weights)
        while left < right - 1:
            mp = (left + right) // 2
            if capacityWorks(mp):
                right = mp
            else:
                left = mp
        return left if capacityWorks(left) else right