from collections import deque
from typing import Counter, List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        

class LastStoneWeight:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 == s2:
                continue
            heapq.heappush(stones, -abs(s1 - s2))
        return -stones[0] if stones else 0


class LeastInterval:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # max heap: most frequent to least
        hp = [-cnt for cnt in count.values()]
        heapq.heapify(hp)

        time = 0
        q = deque() # [-cnt, next avilable time]
        while hp or q:
            time += 1

            if not hp:
                # fast forward to the available time of next available task
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(hp) # decrement count
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                # when task becomes available again, push to heap
                heapq.heappush(hp, q.popleft()[0])

        return time

