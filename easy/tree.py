from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvertTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

class MaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        mdep = 0

        def recurse(n: Optional[TreeNode], depth: int):
            if not n:
                nonlocal mdep
                mdep = max(mdep, depth)
                return

            recurse(n.left, depth+1)
            recurse(n.right, depth+1)

        recurse(root, 0)
        return mdep


class DiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def recurse(n: Optional[TreeNode]) -> int:
            if not n:
                return 0

            ldep = recurse(n.left)
            rdep = recurse(n.right)

            nonlocal dia
            dia = max(dia, ldep + rdep)
            return 1 + max(ldep, rdep)
        
        recurse(root)
        return dia

