from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        snums = sorted(nums)
        partials = [snums[0]]
        for i in range(1, len(nums)):
            partials.append(partials[i-1] + snums[i])

        out = []
        for query in queries:
            if query < partials[0]:
                out.append(0)
                continue
            out.append(1 + max(i for i in range(len(partials)) if query >= partials[i]))
        return out