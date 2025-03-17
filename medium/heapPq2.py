from collections import defaultdict, deque
import heapq
from typing import Counter, List, Set, Tuple


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


class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


class Twitter:
    def __init__(self):
        self.count = 0
        self.follows: dict[int, Set[int]] = defaultdict(set)
        self.tweets: dict[int, List[Tuple[int, int]]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        rs = []
        hp: List[Tuple[int, int, int, int]] = [] # count, tweetId, followeeId, index

        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId not in self.tweets:
                continue
            for (count, tweetId) in self.tweets[followeeId]:
                heapq.heappush(hp, (-count, tweetId, followeeId, len(self.tweets[followeeId])-1))

        while hp and len(rs) < 10:
            nc, tweetId, followeeId, idx = heapq.heappop(hp)
            rs.append(tweetId)
            if nc > 0:
                idx -= 1
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(hp, (-count, tweetId, followeeId, idx))

        return rs

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

