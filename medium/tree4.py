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

