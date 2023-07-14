from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        partial = {arr[0]: 1}
        for i in range(1, len(arr)):
            prev = arr[i] - difference
            run = partial[prev]+1 if prev in partial else 1
            if prev in partial:
                del partial[prev]
            challenger = partial[arr[i]] if arr[i] in partial else 0
            run = max(run, challenger)
            partial[arr[i]] = run
        return max(val for val in partial.values())