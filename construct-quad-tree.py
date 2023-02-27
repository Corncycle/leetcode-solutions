from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def getRegion(x1, x2, y1, y2):
            out = []
            for i in range(y1, y2):
                for j in range(x1, x2):
                    out.append(grid[i][j])
            return out

        def build(x1, x2, y1, y2, parent, parToChildDir):
            if len(set(getRegion(x1, x2, y1, y2))) == 1:
                n = Node(grid[y1][x1], True, None, None, None, None)
                if parent:
                    setattr(parent, parToChildDir, n)
                return n
            n = Node(0, False, None, None, None, None)
            if parent:
                setattr(parent, parToChildDir, n)
            build(x1, (x2 + x1) // 2, y1, (y2 + y1) // 2, n, "topLeft")
            build((x2 + x1) // 2, x2, y1, (y2 + y1) // 2, n, "topRight")
            build(x1, (x2 + x1) // 2, (y2 + y1) // 2, y2, n, "bottomLeft")
            build((x2 + x1) // 2, x2, (y2 + y1) // 2, y2, n, "bottomRight")
            return n

        return build(0, len(grid), 0, len(grid), None, None)