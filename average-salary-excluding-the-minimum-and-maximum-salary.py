from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        minSal, maxSal = salary[0], salary[0]
        total = 0
        for s in salary:
            if s < minSal:
                minSal = s
            if s > maxSal:
                maxSal = s
            total += s
        total = total - minSal - maxSal
        return total / (len(salary) - 2)