from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        out = 1
        for _ in range(k - 1):
            if i < len(arr):
                while i < len(arr) and arr[i] == out:
                    i += 1
                    out += 1
            out += 1
        while i < len(arr) and arr[i] == out:
            i += 1
            out += 1
        return out