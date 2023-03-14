from util import TreeNode
from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def computeNode(node: TreeNode, running: int) -> None:
            if not node.left and not node.right:
                self.total += 10 * running + node.val
                return
            if node.left:
                computeNode(node.left, 10 * running + node.val)
            if node.right:
                computeNode(node.right, 10 * running + node.val)

        if root:
            computeNode(root, 0)
        return self.total
