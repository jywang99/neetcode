from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeWrap:
    def __init__(self, n: ListNode) -> None:
        self.node = n

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        for n in lists:
            if not n:
                continue
            heapq.heappush(hp, NodeWrap(n))

        dummy = n = ListNode()
        while hp:
            nn = heapq.heappop(hp).node
            n.next = nn
            n = n.next
            if nn.next:
                heapq.heappush(hp, NodeWrap(nn.next))

        return dummy.next
        

class ReverseKGroup:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(cur: ListNode, k: int):
            while cur and k>0:
                cur = cur.next
                k -= 1
            return cur

        dummy = ListNode(0, head)
        gprev = dummy

        while True:
            kth = getKth(gprev, k)
            if not kth:
                break
            gnext = kth.next

            prev, cur = kth.next, gprev.next
            while cur != gnext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = gprev.next
            gprev.next = kth
            gprev = tmp

        return dummy.next

