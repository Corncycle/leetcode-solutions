class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        
        while res >= 10:
            n = res
            total = 0
            while n:
                total += n % 10
                n = n // 10
            res = total
        return res