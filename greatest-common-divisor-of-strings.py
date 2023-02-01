from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lengcd = gcd(len(str1), len(str2))
        for i in reversed(range(1, lengcd + 1)):
            if lengcd % i == 0:
                if str2 == str2[:i] * (len(str2) // i) and str1 == str2[:i] * (len(str1) // i):
                    return str2[:i]
        return ""