import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.hp, self.k = nums, k

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]

