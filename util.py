from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)
    
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildBinaryTree(vals):
    root = TreeNode(vals[0])
    frontier = deque([root])
    newFrontier = deque()
    i = 1
    addLeft = True
    while i < len(vals) and frontier:
        if vals[i] is not None:
            if addLeft:
                frontier[0].left = TreeNode(vals[i])
                newFrontier.append(frontier[0].left)
            else:
                frontier[0].right = TreeNode(vals[i])
                newFrontier.append(frontier[0].right)
        if not addLeft:
            frontier.popleft()
        addLeft = not addLeft
        if not frontier:
            frontier = newFrontier
        i += 1
    return root

def printBinaryTree(node):
    levels = [[node]]
    depth = 0
    while not all([n == "." for n in levels[depth]]):
        levels.append([])
        for n in levels[depth]:
            if not n or n == ".":
                levels[depth + 1].append(".")
                levels[depth + 1].append(".")
            else:
                levels[depth + 1].append(n.left if n.left else ".")
                levels[depth + 1].append(n.right if n.right else".")
        depth += 1
    levels.pop()
    step = 2 ** (depth - 1) - 1
    for level in levels:
        print((" " * (step)) + (" " * (2 * (step + 1) - 1)).join([(str(n.val) if type(n) == TreeNode else ".") for n in level]))
        step = (step + 1) // 2 - 1