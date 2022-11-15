from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        current, currentVal = root, 1
        lHeight = self.getHeightOnSide(current, "left")
        rHeight = self.getHeightOnSide(current, "right")
        while True:
            if current.right is None:
                return currentVal if current.left is None else currentVal * 2
            elif lHeight == rHeight:
                # worked this out on paper (formula is nonobvious)
                return 2 ** rHeight * (currentVal + 1) - 1
            rChildLHeight = self.getHeightOnSide(current.right, "left")
            rChildRHeight = rHeight - 1
            if rChildLHeight != rChildRHeight:
                current, currentVal = current.right, currentVal * 2 + 1
                lHeight, rHeight = rChildLHeight, rChildRHeight
            else:
                current, currentVal = current.left, currentVal * 2
                lHeight, rHeight = lHeight - 1, self.getHeightOnSide(current, "right")

    def getHeightOnSide(self, node: TreeNode, side: str) -> int:
        height = 0
        current = node
        while getattr(current, side) != None:
            current = getattr(current, side)
            height += 1
        return height