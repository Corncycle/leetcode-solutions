from typing import Optional
from util import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def areSymmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left or not right:
                return not left and not right
            if left.val != right.val:
                return False
            return (areSymmetric(left.left, right.right) 
                and areSymmetric(left.right, right.left))
        return areSymmetric(root.left, root.right)