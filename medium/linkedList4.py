from typing import List, Optional
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


class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = n = ListNode()
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            n.next = ListNode(s % 10)
            n = n.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return dummy.next


class FindDuplicate:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]

        return s


class CacheNode:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key, self.val = key, val
        self.left: CacheNode = None
        self.right: CacheNode = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = CacheNode(), CacheNode()
        self.left.right, self.right.left = self.right, self.left

    def remove(self, n: CacheNode):
        left, right = n.left, n.right
        left.right, right.left = right, left

    def insert(self, n: CacheNode):
        left, right = self.right.left, self.right
        left.right, right.left = n, n
        n.left, n.right = left, right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        self.remove(n)
        self.insert(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        n = CacheNode(key, value)
        self.insert(n)
        self.cache[key] = n
        if len(self.cache) > self.cap:
            n = self.left.right
            self.remove(n)
            del self.cache[n.key]

