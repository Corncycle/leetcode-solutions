from collections import deque

'''I learned this approach of more concisely keeping track of periods of price
decreases using a stack from the youtube channel Tomothy H Chang.

https://www.youtube.com/watch?v=oFByATk8XrE
'''
class StockSpanner:
    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        if not len(self.stack):
            self.stack.append((price, 1))
        else:
            if self.stack[-1][0] > price:
                self.stack.append((price, 1))
            else:
                numDays = 1
                while self.stack and self.stack[-1][0] <= price:
                    tup = self.stack.pop()
                    numDays += tup[1]
                self.stack.append((price, numDays))
        return self.stack[-1][1]