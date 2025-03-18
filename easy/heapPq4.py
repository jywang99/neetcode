import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.hp, self.k = nums, k

    def add(self, val: int) -> int:

