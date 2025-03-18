from collections import defaultdict, deque
import heapq
from typing import Counter, List


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [[-x**2 + -y**2, x, y] for [x, y] in points]
        heapq.heapify(hp)

        while len(hp) > k:
            heapq.heappop(hp)

        return [[x, y] for [_, x, y] in hp]


class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -nums[0]


class Twitter:
    def __init__(self):
        self.count = 0 # 0, -1, -2, ... because used for MaxHeap
        self.tweetMap = defaultdict(list) # userId -> [[count, tweetIds], ...]
        self.followMap = defaultdict(set) # userId -> {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        rs = []
        # max heap of [count (timestamp), tweetId, followeeId, tweet idx in followee's tweet list]
        hp = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(hp, [count, tweetId, followeeId, index - 1])

        while hp and len(rs) < 10:
            count, tweetId, followeeId, index = heapq.heappop(hp)
            rs.append(tweetId)
            if index >= 0:
                # there are more tweets by this user, so push the next (older) one to heap
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(hp, [count, tweetId, followeeId, index - 1])

        return rs


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


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

