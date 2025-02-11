from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReorderList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f:
            s = s.next
            if not f.next:
                break
            f = f.next.next

        prev, cur = None, s
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        if s:
            s.next = None
        n1, n2 = head, prev
        n = ListNode()
        pick1 = True
        while n2:
            if pick1:
                n.next = n1
                n1 = n1.next
            else:
                n.next = n2
                n2 = n2.next
            n = n.next
            pick1 = not pick1
        n.next = n1
        n1.next = None

