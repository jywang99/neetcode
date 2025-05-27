from collections import deque
from typing import List, Optional


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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"

        rs: List[str] = []
        q: deque[Optional[TreeNode]] = deque([root])
        while q:
            n = q.popleft()
            if not n:
                rs.append("N")
                continue
            rs.append(str(n.val))
            q.append(n.left)
            q.append(n.right)

        return ",".join(rs)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "N":
            return None
        vals = data.split(",")

        root = TreeNode(int(vals[0]))
        q = deque([root])
        idx = 0
        while q:
            n = q.popleft()
            idx += 1
            if vals[idx] != "N":
                n.left = TreeNode(int(vals[idx]))
                q.append(n.left)
            idx += 1
            if vals[idx] != "N":
                n.right = TreeNode(int(vals[idx]))
                q.append(n.right)

        return root

