class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        midpoint = len(s) // 2
        start, end = s[:midpoint].lower(), s[midpoint:].lower()
        vowels = ["a", "e", "i", "o", "u"]
        balance = 0
        for c in vowels:
            balance += start.count(c)
            balance -= end.count(c)
        return balance == 0