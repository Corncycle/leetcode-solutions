from util import TreeNode
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        currNodes = [root]
        sums = []
        while currNodes:
            sums.append(sum(node.val for node in currNodes))
            
            nextNodes = []
            for node in currNodes:
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            currNodes = nextNodes
        return sums.index(max(sums)) + 1