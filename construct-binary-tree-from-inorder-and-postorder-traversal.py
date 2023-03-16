from typing import Optional, List
from util import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(ino: List[int], posto: List[int], parent: Optional[TreeNode], pToChildDir: Optional[str]) -> Optional[TreeNode]:
            if not ino:
                return
            node = TreeNode(posto[-1])
            if parent:
                setattr(parent, pToChildDir, node)
            i = ino.index(posto[-1])
            if i > 0:
                build(ino[:i], posto[:i], node, "left")
            if i < len(ino) - 1:
                build(ino[i+1:], posto[i:-1], node, "right")
            return node
        return build(inorder, postorder, None, None)