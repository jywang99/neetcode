from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReorderList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        prev, cur = None, s.next
        s.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        list1, list2 = head, prev
        n = ListNode()
        pick1 = True
        while list2:
            if pick1:
                n.next = list1
                list1 = list1.next
            else:
                n.next = list2
                list2 = list2.next
            pick1 = not pick1
            n = n.next
        n.next = list1


class RemoveNthFromEnd:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = ListNode(next=head), head
        dummy = l

        for _ in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyRandomList:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        doppel = defaultdict(lambda: Node(0))
        doppel[None] = None
        n = head
        while n:
            doppel[n].val = n.val
            doppel[n].next = doppel[n.next]
            doppel[n].random = doppel[n.random]
            n = n.next
        return doppel[head]

