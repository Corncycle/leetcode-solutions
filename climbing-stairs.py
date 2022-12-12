class Solution:
    def climbStairs(self, n: int) -> int:
        counts = [1, 2]
        while len(counts) < n:
            counts.append(counts[-1] + counts[-2])
        return counts[n - 1]

s = Solution()
print(s.climbStairs(5))