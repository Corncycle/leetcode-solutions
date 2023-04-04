class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        count = 1
        for c in s:
            if c in curr:
                curr = set()
                count += 1
            curr.add(c)
        return count