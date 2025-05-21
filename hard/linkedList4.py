import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        
