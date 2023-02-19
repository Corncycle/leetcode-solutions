from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.out = [[root.val]]
        def traverse(prev, direction):
            newPrev = []
            for node in prev:
                if node.left:
                    newPrev.append(node.left)
                if node.right:
                    newPrev.append(node.right)
            if newPrev:
                if direction == "ltr":
                    self.out.append([node.val for node in newPrev])
                else:
                    self.out.append([node.val for node in reversed(newPrev)])
                traverse(newPrev, "ltr" if direction == "rtl" else "rtl")
        traverse([root], "rtl")
        return self.out