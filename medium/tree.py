from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestor:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


class LevelOrder:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rs = []

        def recurse(n: Optional[TreeNode], depth: int):
            if not n:
                return
            if depth == len(rs):
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
            if not n:
                return

            if len(rs) == depth:
                rs.append(n.val)

            recurse(n.right, depth+1)
            recurse(n.left, depth+1)

        recurse(root, 0)
        return rs

