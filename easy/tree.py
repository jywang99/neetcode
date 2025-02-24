from typing import Optional, Tuple


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


class BalancedTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(n: Optional[TreeNode]) -> Tuple[bool, int]:
            if not n:
                return True, 0
            
            lb, ld = recurse(n.left)
            rb, rd = recurse(n.right)
            balanced = lb and rb and abs(rd - ld) <= 1

            return balanced, max(ld, rd) + 1

        return recurse(root)[0]


class IsSameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class IsSubtree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

