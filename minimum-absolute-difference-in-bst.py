from typing import Optional
from util import TreeNode

class Solution:
    def __init__(self):
        self.vals = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def populateVals(node): 
            if node:
                populateVals(node.left)
                self.vals.append(node.val)
                populateVals(node.right)
        populateVals(root)
        
        return min(self.vals[i]-self.vals[i-1] for i in range(1, len(self.vals)))