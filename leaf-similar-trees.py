from typing import Optional, List
from util import TreeNode

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = [[root1], [root2]]
        newLeaves = [self.iterate(leaves[0]), self.iterate(leaves[1])]
        for i in range(2):
            while newLeaves[i] != leaves[i]:
                leaves[i] = newLeaves[i]
                newLeaves[i] = self.iterate(leaves[i])
        if len(newLeaves[0]) != len(newLeaves[1]):
            return False
        return all([l1.val == l2.val for l1, l2 in zip(newLeaves[0], newLeaves[1])])
        
    def iterate(self, currNodes: List[TreeNode]) -> List[TreeNode]:
        out = []
        for node in currNodes:
            if not node.left and not node.right:
                out.append(node)
            else:
                out.append(node.left) if node.left else None
                out.append(node.right) if node.right else None
        return out