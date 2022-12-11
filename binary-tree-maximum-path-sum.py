from typing import Optional
from util import *

'''The idea for this solution is that every path through the tree contains a
unique topmost node. Thus, to each node in the tree we can associate a leftSum
and rightSum, indicating the best sums achieved by beginning at the node and
immediately moving left or right respectively. Then we simply need to find the
node with the highest leftSum and rightSum, which combine to give a path.
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sideSums(root)
        
        pathSizes = []
        def maxPath(node: Optional[TreeNode]) -> None:
            pathSizes.append(node.val + node.leftSum + node.rightSum)
            maxPath(node.left) if node.left else None
            maxPath(node.right) if node.right else None
        maxPath(root)

        return max(pathSizes)

    def sideSums(self, node: TreeNode) -> None:
        if node.left:
            node.leftSum = max(node.left.val + max(*self.sideSums(node.left), 0), 0)
        else:
            node.leftSum = 0
        if node.right:
            node.rightSum = max(node.right.val + max(*self.sideSums(node.right), 0), 0)
        else:
            node.rightSum = 0
        return (node.leftSum, node.rightSum)