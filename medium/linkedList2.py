from collections import defaultdict
from typing import List, Optional


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


class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = n = ListNode()
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = 1 if s >= 10 else 0
            n.next = ListNode(s % 10)
            n = n.next
            l1 = l1.next
            l2 = l2.next

        e = l1 or l2
        while e:
            s = e.val + carry
            carry = 1 if s >= 10 else 0
            n.next = ListNode(s % 10)
            n = n.next
            e = e.next

        if carry > 0:
            n.next = ListNode(1)
        
        return dummy.next


class FindDuplicate:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        b = 0
        while True:
            if nums[s] == nums[b]:
                return nums[s]
            s = nums[s]
            b = nums[b]



class CacheNode:
    def __init__(self, key: int = -1, val: int = -1) -> None:
        self.key = key
        self.val = val
        self.left: None|CacheNode = None
        self.right: None|CacheNode = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, CacheNode] = {}
        self.left, self.right = CacheNode(), CacheNode()
        self.left.right, self.right.left = self.right, self.left

    def remove(self, n: CacheNode):
        left, right = n.left, n.right
        left.right, right.left = right, left

    def insert(self, n: CacheNode):
        left, right = self.right.left, self.right
        n.left, n.right = left, right
        left.right, right.left = n, n

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
            lru = self.left.right
            self.remove(lru)
            del self.cache[lru.key]

