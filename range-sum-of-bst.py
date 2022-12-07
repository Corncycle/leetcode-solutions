from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        children = (self.rangeSumBST(root.left, low, high) + 
            self.rangeSumBST(root.right, low, high))
        return children + root.val if low <= root.val <= high else children