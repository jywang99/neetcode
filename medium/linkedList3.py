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

