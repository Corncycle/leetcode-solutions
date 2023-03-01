from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def helper(ns: List[int]) -> None:
            if len(ns) == 1:
                return
            left = ns[:len(ns) // 2]
            right = ns[len(ns) // 2:]
            helper(left)
            helper(right)
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ns[i+j] = left[i]
                    i += 1
                else:
                    ns[i+j] = right[j]
                    j += 1
            if i < len(left):
                ns[i+j:] = left[i:]
            elif j < len(right):
                ns[i+j:] = right[j:]
        helper(nums)
        return nums