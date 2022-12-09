from typing import Optional
from util import *

null = None

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxFound = 0
        frontier = [root]
        while frontier:
            newFrontier = []
            for node in frontier:
                maxFound = max(maxFound, self.maxFrom(node))
                if node.left:
                    newFrontier.append(node.left)
                if node.right:
                    newFrontier.append(node.right)
            frontier = newFrontier
        return maxFound

    def maxFrom(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 0
        maxFound = 0
        frontier = [root.left, root.right]
        frontier = [node for node in frontier if node]
        while frontier:
            newFrontier = []
            for node in frontier:
                diff = self.nodeDiff(root, node)
                maxFound = max(maxFound, diff)
                if node.left:
                    newFrontier.append(node.left)
                if node.right:
                    newFrontier.append(node.right)
            frontier = newFrontier
        return maxFound
    
    def nodeDiff(self, n1: TreeNode, n2: TreeNode) -> int:
        return abs(n1.val - n2.val)