from typing import Optional, List
from util import TreeNode

# the idea to serialize the trees was taken from the following solution:
# https://leetcode.com/problems/find-duplicate-subtrees/solutions/3238153/python3-easy-solution-compare-serialisations-of-treenodes/
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(n: Optional[TreeNode], data: List[str]) -> None:
            if not n:
                data.append("#,")
                return
            data.append(str(n.val))
            data.append(",")
            serialize(n.left, data)
            serialize(n.right, data)

        trees = {}
        counts = {}
        def search(node: Optional[TreeNode]) -> None:
            if not node:
                return
            d = []
            serialize(node, d)
            nSer = "".join(d)
            if nSer not in trees:
                trees[nSer] = node
                counts[nSer] = 1
            else:
                counts[nSer] += 1
            search(node.left)
            search(node.right)
        
        search(root)
        return [trees[tree] for tree in trees if counts[tree] > 1]