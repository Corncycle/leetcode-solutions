from typing import List

# This approach is due to the editorial for the problem:
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/editorial/

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        sortedPairs = sorted(zip(nums, cost))
        sNums = [t[0] for t in sortedPairs]
        sCost = [t[1] for t in sortedPairs]
        n = len(nums)

        best = sum((sNums[i]-sNums[0]) * sCost[i] for i in range(n))
        curr = best
        pref = 0
        suff = sum(sCost)

        for i in range(1, n):
            pref += sCost[i-1]
            suff -= sCost[i-1]

            delta = sNums[i]-sNums[i-1]
            if delta > 0:
                curr += delta * pref
                curr -= delta * suff
                best = min(curr, best)

        return best