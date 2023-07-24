class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or x == 0:
            return x
        out = 1
        remaining = abs(n)
        currPow = x
        while remaining:
            if remaining % 2 == 1:
                out *= currPow
            remaining = remaining // 2
            currPow = currPow * currPow
        return out if n >= 0 else 1 / out