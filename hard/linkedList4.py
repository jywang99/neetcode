import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode|None = next


class NodeWrap:
    def __init__(self, node: ListNode) -> None:
        self.node = node

    def __lt__(self, other: 'NodeWrap') -> bool:
        return self.node.val < other.node.val


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
        def get_kth(n: ListNode|None) -> Optional[ListNode]:
            kk = k
            while n and kk:
                n = n.next
                kk -= 1
            return n

        dummy = gprev = ListNode(next=head)
        while True:
            kth = get_kth(gprev)
            if not kth:
                break
            gnext = kth.next

            prev, curr = gnext, gprev.next
            while curr and curr != gnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = gprev.next
            gprev.next = kth
            gprev = tmp

        return dummy.next

