import math

class Solution:
    def maximum69Number (self, num: int) -> int:
        numDigits = math.floor(math.log10(num))
        for i in range(numDigits, -1, -1):
            if num // 10 ** i % 10 == 6:
                return num + 3 * 10 ** i
        return num