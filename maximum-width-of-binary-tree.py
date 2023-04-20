from util import TreeNode
from typing import Optional
from collections import deque

# this bfs approach is given by
# https://leetcode.com/problems/maximum-width-of-binary-tree/solutions/3437541/python3-bfs-easy-solution-clearly-explained/

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = deque([[root, 0]])
        maxWidth = 1

        while d:
            maxWidth = max(maxWidth, d[-1][1] - d[0][1] + 1)
            dlen = len(d)
            for _ in range(dlen):
                curr, pos = d.popleft()
                if curr.left:
                    d.append([curr.left, 2 * pos])
                if curr.right:
                    d.append([curr.right, 2 * pos + 1])
            
        return maxWidth