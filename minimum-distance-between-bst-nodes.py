from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def treeToList(root):
            if not root:
                return []
            return treeToList(root.left) + [root.val] + treeToList(root.right)
        
        fullList = treeToList(root)
        return min(fullList[i] - fullList[i-1] for i in range(1, len(fullList)))