from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFound = 1
        start, end = 0, 1
        basket = set(fruits[start:end])
        counter = Counter([fruits[0]])
        while end < len(fruits):
            if len(basket) < 2:
                counter[fruits[end]] += 1
                basket.add(fruits[end])
                end += 1
                maxFound = max(maxFound, end-start)
            else:
                if fruits[end] in basket:
                    counter[fruits[end]] += 1
                    end += 1
                    maxFound = max(maxFound, end-start)
                else:
                    if counter[fruits[start]] == 1:
                        basket.remove(fruits[start])
                    counter[fruits[start]] -= 1
                    start += 1
        return maxFound