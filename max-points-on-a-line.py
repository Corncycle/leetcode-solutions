from typing import List

class Solution:
    # brute force solution: just take all pairs of points and count how many
    # points lie on the line between them. can probably optimize by caching
    # previously computed lines

    # a point (a, b) lies on the line between (x0, y0) and (x1, y1) iff
    # (b - y1)(x1 - x0) == (a - x1)(y1 - y0)
    def maxPoints(self, points: List[List[int]]) -> int:
        maxFound = min(len(points), 2)
        for i in range(len(points)):
            x0, y0 = points[i]
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                dx, dy = x1 - x0, y1 - y0
                count = 0
                for point in points:
                    a, b = point
                    if (b - y1) * dx == (a - x1) * dy:
                        count += 1
                if count > (len(points)) // 2:
                    return count
                if count > maxFound:
                    maxFound = count
        return maxFound