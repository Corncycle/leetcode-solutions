class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return [0, 1, 1][n]
        memory = [0, 1, 1, 2]
        for _ in range(n - 3):
            for j in range(1, 4):
                memory[j-1] = memory[j]
            memory[-1] = memory[0] + memory[1] + memory[2]
        return memory[-1]