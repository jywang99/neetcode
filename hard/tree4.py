from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class MaxPathSum:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        rs = root.val if root else 0
        def recurse(n: Optional[TreeNode]) -> int:
            if not n:
                return 0

            lmax = max(0, recurse(n.left))
            rmax = max(0, recurse(n.right))

            nonlocal rs
            rs = max(rs, n.val + lmax + rmax)
            return n.val + max(lmax, rmax)

        recurse(root)
        return rs

