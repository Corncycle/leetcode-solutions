'''Lagrange's four squares theorem states that the output is bounded above by 4
so it suffices to check if n is a sum of 1, 2, or 3 squares. The commented
solution is slower but simpler
'''

class Solution:
    def numSquares(self, n: int) -> int:
        if n == int(n ** 0.5) ** 2:
            return 1
        squares = [n ** 2 for n in range(1, int(n ** 0.5) + 1)]
        twoSquares = set()
        for s1 in squares:
            for s2 in squares:
                twoSquares.add(s1 + s2)
        if n in twoSquares:
            return 2
        threeSquares = set()
        for s1 in twoSquares:
            for s2 in squares:
                threeSquares.add(s1 + s2)
        return 3 if n in threeSquares else 4

'''class Solution:
    def numSquares(self, n: int) -> int:
        squares = [n ** 2 for n in range(int(n ** 0.5) + 1)]
        sums = {}
        for s1 in squares:
            for s2 in squares:
                for s3 in squares:
                    sums[s1 + s2 + s3] = min(3 - [s1, s2, s3].count(0), sums.get(s1 + s2 + s3, 4))
        return sums.get(n, 4)'''