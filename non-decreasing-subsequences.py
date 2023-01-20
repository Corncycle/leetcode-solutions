from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seqs = set()
        for num in nums:
            newSeqs = set()
            for seq in seqs:
                if seq[-1] <= num:
                    newSeqs.add(seq + (num,))
            seqs |= newSeqs
            seqs.add((num,))
        return [list(seq) for seq in seqs if len(seq) > 1]