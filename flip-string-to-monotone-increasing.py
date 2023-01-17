from collections import Counter

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        c = Counter(s)

        def getUnbalance(left, right, s):
            l, r = 0, 0
            while s[left + l] == "1":
                l += 1
            while s[right - r] == "0":
                r += 1
            return l, r

        left, right = 0, len(s) - 1
        minFound = min(c["0"], c["1"])
        curr = 0
        while left < right:
            if s[left] == "0":
                left += 1
                c["0"] -= 1
                continue
            if s[right] == "1":
                right -= 1
                c["1"] -= 1
                continue
            minFound = min(minFound, curr + c["0"], curr + c["1"])
            l, r = getUnbalance(left, right, s)
            curr += l + r
            left += l
            right -= r
            c["1"] -= l
            c["0"] -= r
        return min(curr, minFound)