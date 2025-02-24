from typing import Optional
from collections import defaultdict


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode|None' = None):
        self.val = val
        self.next = next


class HasCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


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

        l1, l2 = head, prev
        c1 = True
        dummy = n = ListNode(0)
        while l1 or l2:
            if c1:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
            c1 = not c1

        return dummy.next


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
    def __init__(self, x: int, next: 'Node|None' = None, random: 'Node|None' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyRandomList:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        doppel = defaultdict(lambda: Node(0))
        doppel[None] = None

        n = head
        while n:
            doppel[n].val = n.val
            doppel[n].next = doppel[n.next]
            doppel[n].random = doppel[n.random]
            n = n.next

        return doppel[head]

