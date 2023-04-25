from bisect import insort

class SmallestInfiniteSet:
    def __init__(self):
        self.missing = []

    def popSmallest(self) -> int:
        i = 0
        while i < len(self.missing):
            if self.missing[i] > i+1:
                insort(self.missing, i+1)
                return i+1
            i += 1
        insort(self.missing, i+1)
        return i+1

    def addBack(self, num: int) -> None:
        if num in self.missing:
            self.missing.remove(num)