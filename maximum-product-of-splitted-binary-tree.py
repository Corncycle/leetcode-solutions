from typing import Optional
from util import *

# This solution is due to leetcode user thezealott
# I had tried employing a similar but less elegant solution on my own, but
# it timed out repeatedly on test 52/54. Even this solution (which is accepted
# on leetcode) fails to run on this test on my machine due to Python's default
# recursion depth limit. I could try changing the recursion depth limit but I
# don't know exactly what could go wrong if I do so I'm not going to.
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def treeSums(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            nodeSum = node.val + treeSums(node.left) + treeSums(node.right)
            sums.append(nodeSum)
            return nodeSum

        rootSum = treeSums(root)
        return max((rootSum - s) * s for s in sums) % (10 ** 9 + 7)