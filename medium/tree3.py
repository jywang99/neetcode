from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LevelOrder:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rs = []

        def recurse(n: Optional[TreeNode], depth: int):
            if not n:
                return
            if len(rs) == depth:
                rs.append([])

            rs[depth].append(n.val)
            recurse(n.left, depth + 1)
            recurse(n.right, depth + 1)

        recurse(root, 0)
        return rs


class RightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rs = []

        def recurse(n: Optional[TreeNode], depth: int):
            nonlocal rs
            if not n:
                return

            if len(rs) == depth:
                rs.append(n.val)

            depth += 1
            recurse(n.right, depth)
            recurse(n.left, depth)

        recurse(root, 0)
        return rs

class GoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        def recurse(n: Optional[TreeNode], msf: float) -> int:
            if not n:
                return 0

            g = 0
            if n.val >= msf:
                g = 1
                msf = n.val
            lg = recurse(n.left, msf)
            rg = recurse(n.right, msf)

            return g + lg + rg

        return recurse(root, -float("inf"))


class LowestCommonAncestor:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

