from util import TreeNode
from typing import Optional

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def getLeftZz(node):
            if not hasattr(node, "leftzz"):
                node.leftzz = 1 + getRightZz(node.left) if node.left else 0
            return node.leftzz
        
        def getRightZz(node):
            if not hasattr(node, "rightzz"):
                node.rightzz = 1 + getLeftZz(node.right) if node.right else 0
            return node.rightzz

        self.best = 0

        def getBestZz(node):
            if not node:
                return
            self.best = max(self.best, getLeftZz(node), getRightZz(node))
            getBestZz(node.left)
            getBestZz(node.right)
        
        getBestZz(root)
        return self.best