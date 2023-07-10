from typing import Optional
from util import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        frontier = [root]
        depth = 0
        while True:
            depth += 1
            newFrontier = []
            for node in frontier:
                if not (node.left or node.right):
                    return depth
                if node.left:
                    newFrontier.append(node.left)
                if node.right:
                    newFrontier.append(node.right)
            frontier = newFrontier