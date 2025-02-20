from typing import List, Optional
from collections import defaultdict
import math


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


class RemoveNthFromEnd:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyRandomList:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        doppel: dict[Node|None, Node|None] = defaultdict(lambda: Node(0))
        doppel[None] = None

        cur = head
        while cur:
            doppel[cur].val = cur.val
            doppel[cur].next = doppel[cur.next]
            doppel[cur].random = doppel[cur.random]
            cur = cur.next

        return doppel[head]


class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        dummy = n = ListNode()
        while l1 and l2:
            digit = (1 if carry else 0) + l1.val + l2.val
            carry = math.floor(digit / 10) == 1
            n.next = ListNode(digit % 10)
            n = n.next
            l1 = l1.next
            l2 = l2.next

        extra = l1 or l2
        while extra:
            digit = (1 if carry else 0) + extra.val
            carry = math.floor(digit / 10) == 1
            n.next = ListNode(digit % 10)
            n = n.next
            extra = extra.next

        if carry:
            n.next = ListNode(1)

        return dummy.next


class FindDuplicate:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while f < len(nums):
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s


class CacheNode:
    def __init__(self, key: int, val: int) -> None:
        self.key, self.val = key, val
        self.left, self.right = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, CacheNode] = {}
        self.left, self.right = CacheNode(0, 0), CacheNode(0, 0)
        self.left.right = self.right
        self.right.left = self.left

    def insert(self, node: CacheNode):
        left, right = self.right.left, self.right
        node.left, node.right = left, right
        left.right, right.left = node, node

    def remove(self, node: CacheNode):
        left, right = node.left, node.right
        left.right = right
        right.left = left

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
        self.cache[key] = n
        self.insert(n)

        if len(self.cache) > self.cap:
            lru = self.left.right
            self.remove(self.left.right)
            del self.cache[lru.key]

