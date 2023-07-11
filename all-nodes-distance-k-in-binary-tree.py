from typing import List, Optional
from util import TreeNode

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        distances = {}
        # populate distances for all nodes from target up to root
        def populateInitialDistances(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node.val == target.val:
                distances[node.val] = 0
                return 0
            leftres = -1
            rightres = -1
            if node.left:
                leftres = populateInitialDistances(node.left)
            if node.right:
                rightres = populateInitialDistances(node.right)
            res = max(leftres, rightres)
            if res > -1:
                distances[node.val] = res + 1
                return res + 1
            return -1
        populateInitialDistances(root)

        # now all distances can be obtained by traversing up until a node with known distance is reached
        def populateAllDistances(node: Optional[TreeNode], parentDistance: int):
            if not node:
                return
            if not (node.val in distances):
                distances[node.val] = parentDistance + 1
            if node.left:
                populateAllDistances(node.left, distances[node.val])
            if node.right:
                populateAllDistances(node.right, distances[node.val])
        populateAllDistances(root, distances[root.val])

        return [val for val in distances.keys() if distances[val] == k]