from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeWrap:
    def __init__(self, n: ListNode) -> None:
        self.node = n

    def __lt__(self, o: 'NodeWrap') -> bool:
        return self.node.val < o.node.val


class MergeKLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp: List[NodeWrap] = []
        for n in lists:
            if not n:
                continue
            heapq.heappush(hp, NodeWrap(n))

        dummy = n = ListNode()
        while hp:
            nn = heapq.heappop(hp).node
            n.next = nn
            if nn.next:
                heapq.heappush(hp, NodeWrap(nn.next))
            n = n.next

        return dummy.next


class ReverseKGroup:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(n: Optional[ListNode]):
            kk = k
            while n and kk:
                n = n.next
                kk -= 1
            return n

        dummy = gprev = ListNode(0, head)
        while True:
            kth = getKth(gprev)
            if not kth:
                break
            gnext = kth.next

            prev, cur = gnext, gprev.next
            while cur != gnext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = gprev.next
            gprev.next = kth
            gprev = tmp

        return dummy.next
        
