from typing import List
from heapq import heapify, heappush, heappop

# this approach is given by the editorial for the problem
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/editorial/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        candidates = [(nums1[0]+nums2[0], 0, 0)]
        visited = {(0, 0)}
        heapify(candidates)
        pairs = []

        for _ in range(k):
            if not candidates:
                return pairs
            __, i, j = heappop(candidates)
            pairs.append([nums1[i], nums2[j]])
            if i < m-1:
                if (i+1, j) not in visited:
                    heappush(candidates, (nums1[i+1]+nums2[j], i+1, j))
                    visited.add((i+1, j))
            if j < n-1:
                if (i, j+1) not in visited:
                    heappush(candidates, (nums1[i]+nums2[j+1], i, j+1))
                    visited.add((i, j+1))

        return pairs