from util import TreeNode
from typing import Optional

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        currLevel = [root]
        while True:
            if any(node == None for node in currLevel):
                break
            nextLevel = []
            for node in currLevel:
                nextLevel.append(node.left)
                nextLevel.append(node.right)
            currLevel = nextLevel
        foundNone = False
        for node in currLevel:
            if not node:
                foundNone = True
                continue
            if foundNone:
                return False
            if node.left or node.right:
                return False
        return True