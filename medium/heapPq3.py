from collections import defaultdict, deque
import heapq
from typing import Counter, List, Set, Tuple


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


class Twitter:
    def __init__(self):
        self.time = 0
        self.follows: dict[int, Set[int]] = defaultdict(set)
        self.tweets: dict[int, List[(Tuple[int, int])]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        rs = []

        self.follows[userId].add(userId)
        for fid in self.follows[userId]:
            twts = self.tweets[fid]
            if not twts:
                continue
            idx = len(twts)-1
            time, twid = twts[idx]
            heapq.heappush(hp, (-time, fid, twid, idx))

        while hp and len(rs) < 10:
            _, fid, twid, idx = heapq.heappop(hp)
            rs.append(twid)
            if idx > 0:
                idx -= 1
                time, twid = self.tweets[fid][idx]
                heapq.heappush(hp, (-time, fid, twid, idx))

        return rs

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

