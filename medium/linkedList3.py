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

        l1, l2 = head, prev
        n = ListNode()
        pick1 = True
        while l1 and l2:
            if pick1:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            pick1 = not pick1
            n = n.next
        n.next = l1 or l2


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
        nmap = defaultdict(lambda: Node(0))
        nmap[None] = None
        n = head
        while n:
            nmap[n].val = n.val
            nmap[n].next = nmap[n.next]
            nmap[n].random = nmap[n.random]
            n = n.next
        return nmap[head]


class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = n = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0

            s = v1 + v2 + carry
            carry = s // 10
            n.next = ListNode(s % 10)
            
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            n = n.next

        return dummy.next

