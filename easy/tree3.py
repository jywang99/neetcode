from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def recurse(n: Optional[TreeNode]) -> int:
            if not n:
                return 0

            ld = recurse(n.left)
            rd = recurse(n.right)
            nonlocal dia
            dia = max(dia, ld + rd)

            return 1 + max(ld, rd)

        recurse(root)
        return dia


class MaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class InvertTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


class BalancedTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(n: Optional[TreeNode]) -> Tuple[int, bool]:
            if not n:
                return 0, True

            ld, lb = recurse(n.left)
            rd, rb = recurse(n.right)

            bal = lb and rb and abs(ld - rd) <= 1
            return 1 + max(ld, rd), bal

        return recurse(root)[1]


class IsSubtree:
    def isSameTree(self, root: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
        if not root and not other:
            return True
        if not root or not other:
            return False
        if root.val != other.val:
            return False
        return self.isSameTree(root.left, other.left) and self.isSameTree(root.right, other.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


class IsSameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

