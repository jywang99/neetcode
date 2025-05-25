import heapq


class MedianFinder:
    def __init__(self):
        self.less = []
        self.more = []

    def addNum(self, num: int) -> None:
        if self.more and num < self.more[0]:
            heapq.heappush(self.less, -num)
        else:
            heapq.heappush(self.more, num)
        ll, ml = len(self.less), len(self.more)
        if ll + 1 < ml:
            heapq.heappush(self.less, -heapq.heappop(self.more))
        elif ll > ml + 1:
            heapq.heappush(self.more, -heapq.heappop(self.less))

    def findMedian(self) -> float:
        ll, ml = len(self.less), len(self.more)
        if ll < ml:
            return self.more[0]
        if ml < ll:
            return -self.less[0]
        return (-self.less[0] + self.more[0]) / 2

