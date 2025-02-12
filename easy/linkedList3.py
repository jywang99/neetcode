from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


class MergeTwoLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = n = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                n.next = list1
                list1 = list1.next
            else:
                n.next = list2
                list2 = list2.next
            n = n.next
        n.next = list1 or list2

        return dummy.next


class HasCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        s, f = head, head.next
        while f and f.next:
            if s == f:
                return True
            s = s.next
            f = f.next.next

        return False

