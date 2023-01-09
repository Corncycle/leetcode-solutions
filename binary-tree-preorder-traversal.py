from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: TreeNode):
            yield node
            if node.left:
                yield from preorder(node.left)
            if node.right:
                yield from preorder(node.right)

        return [node.val for node in preorder(root)] if root else []