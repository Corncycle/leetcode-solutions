import random

class RandomizedSet:
    def __init__(self):
        self.vals = set()
        self.length = 0

    def insert(self, val: int) -> bool:
        oldLength = self.length
        self.vals.add(val)
        self.length = len(self.vals)
        return oldLength != self.length

    def remove(self, val: int) -> bool:
        if val in self.vals:
            self.vals.remove(val)
            self.length -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.vals))