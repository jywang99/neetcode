from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class InvertTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class DiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def recurse(n: Optional[TreeNode]) -> int:
            if not n:
                return 0

            ld, rd = recurse(n.left), recurse(n.right)
            nonlocal dia
            dia = max(dia, ld + rd)
            return 1 + max(ld, rd)

        recurse(root)
        return dia


class BalancedTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(n: Optional[TreeNode]) -> Tuple[bool, int]:
            if not n:
                return True, 0

            lb, ld = recurse(n.left)
            rb, rd = recurse(n.right)

            bal = lb and rb and abs(ld - rd) <= 1
            return bal, 1 + max(ld, rd)

        return recurse(root)[0]

