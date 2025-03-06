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
            recurse(n.left, depth+1)
            recurse(n.right, depth+1)

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


class GoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        def recurse(n: Optional[TreeNode], msf: float) -> int:
            if not n:
                return 0

            good = 0
            if n.val >= msf:
                good = 1
                msf = n.val

            good += recurse(n.left, msf)
            good += recurse(n.right, msf)
            return good
        
        return recurse(root, -float("inf"))

