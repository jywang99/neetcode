from collections import deque
import heapq
from typing import Counter, List


class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [[-(x**2 + y**2), x, y] for [x, y] in points]
        heapq.heapify(hp)

        while len(hp) > k:
            heapq.heappop(hp)
        return [[x, y] for [_, x, y] in hp]


class LeastInterval:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        hp = [-c for c in cnt.values()]
        heapq.heapify(hp)

        time = 0
        q = deque() # time, count
        while hp or q:
            time += 1

            if not hp:
                time = q[0][0]
            else:
                t = heapq.heappop(hp)
                t += 1
                if t < 0:
                    q.append((time + n, t))

            if q and q[0][0] == time:
                t = q.popleft()
                heapq.heappush(hp, t[1])

        return time

