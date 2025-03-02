from typing import List, Optional, Tuple


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


class GoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def recurse(n: Optional[TreeNode], msf: float):
            if not n:
                return

            if msf <= n.val:
                nonlocal cnt
                cnt += 1
                msf = n.val

            recurse(n.left, msf)
            recurse(n.right, msf)

        recurse(root, -float('inf'))
        return cnt


class ValidBST:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(n: Optional[TreeNode], lower: float, upper: float) -> bool:
            if not n:
                return True
            if not (lower < n.val < upper):
                return False

            return recurse(n.left, lower, n.val) and recurse(n.right, n.val, upper)

        return recurse(root, -float("inf"), float("inf"))


class KthSmallest:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rs = None
        cnt = k

        def recurse(n: Optional[TreeNode]):
            nonlocal rs, cnt

            if not n:
                return

            recurse(n.left)
            cnt -= 1
            if cnt == 0:
                rs = n.val
                return
            recurse(n.right)

        recurse(root)
        return rs


class KthSmallestIter:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        cur = root

        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()

            k -= 1
            if k == 0:
                return cur.val

            cur = cur.right


class BuildTree:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indict = { val: key for key, val in enumerate(inorder) }
        pi = 0

        def recurse(l: int, r: int) -> Optional[TreeNode]:
            nonlocal pi
            if l > r:
                return None

            val = preorder[pi]
            pi += 1
            n = TreeNode(val)
            m = indict[val]
            n.left = recurse(l, m-1)
            n.right = recurse(m+1, r)
            return n
        
        return recurse(0, len(inorder)-1)

