# this is a classic recurrence relation problem, relations found by drawing
class Solution:
    def numTilings(self, n: int) -> int:
        # a[i] == # ways fo tile an n x 2 board
        # b[i] == # ways to tile an n x 2 board with 1 tile sticking out
        a = [0, 1, 2]
        b = [0, 1, 2]
        while len(a) < n + 1:
            i = len(a)
            a.append(a[i-1] + a[i-2] + 2 * b[i-2])
            b.append(a[i-1] + b[i-1])
        return a[n] % (10 ** 9 + 7)