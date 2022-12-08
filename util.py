class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

def buildBinaryTree(vals):
    root = TreeNode(vals[0])
    curr = [root]
    i = 1
    while i < len(vals):
        newCurr = []
        for node in curr:
            if i >= len(vals):
                return root
            if vals[i]:
                node.left = TreeNode(vals[i])
                newCurr.append(node.left)
            i += 1
            if vals[i]:
                node.right = TreeNode(vals[i])
                newCurr.append(node.right)
            i += 1
        curr = newCurr
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