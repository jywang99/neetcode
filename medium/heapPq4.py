from collections import defaultdict, deque
import heapq
from typing import Counter, List, Set, Tuple


class LastStoneWeight:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 != s2:
                heapq.heappush(stones, -abs(s1-s2))
        return -stones[0] if stones else 0
        

class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[-(x**2 + y**2), x, y] for [x, y] in points]
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)
        return [[x, y] for [_, x, y] in points]


class TaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        hp = [-v for v in cnt.values()]
        heapq.heapify(hp)

        time = 0
        q = deque() # remainging, revive time
        while hp or q:
            time += 1

            if not hp:
                time = q[0][1]
            else:
                nt = heapq.heappop(hp)
                if nt < -1:
                    q.append((nt+1, time+n))

            if q and time == q[0][1]:
                heapq.heappush(hp, q.popleft()[0])

        return time


class Twitter:
    def __init__(self):
        self.time = 0
        self.follows: dict[int, Set[int]] = defaultdict(set)
        self.tweets: dict[int, List[Tuple[int, int]]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        self.follows[userId].add(userId)
        for fid in self.follows[userId]:
            if not self.tweets[fid]:
                continue
            idx = len(self.tweets[fid]) - 1
            time, twid = self.tweets[fid][idx]
            heapq.heappush(hp, (-time, fid, idx, twid))

        rs = []
        while hp and len(rs) < 10:
            _, fid, idx, twid = heapq.heappop(hp)
            rs.append(twid)
            if idx > 0:
                idx -= 1
                time, twid = self.tweets[fid][idx]
                heapq.heappush(hp, (-time, fid, idx, twid))
        return rs

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

