from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        intres = int("".join(str(n) for n in num)) + k
        return [int(ch) for ch in str(intres)]