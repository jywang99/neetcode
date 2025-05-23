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

        if len(self.less) - len(self.more) > 1:
            heapq.heappush(self.more, -heapq.heappop(self.less))
        elif len(self.more) - len(self.less) > 1:
            heapq.heappush(self.less, -heapq.heappop(self.more))

    def findMedian(self) -> float:
        if len(self.less) == 0 and len(self.more) == 0:
            return 0
        if len(self.less) > len(self.more):
            return -self.less[0]
        if len(self.less) < len(self.more):
            return self.more[0]
        return (-self.less[0] + self.more[0]) / 2

