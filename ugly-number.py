class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        n = n
        for divisor in [2, 3, 5]:
            while n % divisor == 0:
                n //= divisor
        return n == 1