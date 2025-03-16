from collections import deque
import heapq
from typing import Counter, List


class LeastInterval:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        hp = [-c for c in count.values()]
        heapq.heapify(hp)

        time = 0
        q = deque()
        while hp or q:
            time += 1

            if not hp:
                time = q[0][1]
            else:
                cnt = heapq.heappop(hp) + 1
                if cnt < 0:
                    q.append((cnt, time + n))

            if q and  q[0][1] == time:
                heapq.heappush(hp, q.popleft()[0])
        
        return time

