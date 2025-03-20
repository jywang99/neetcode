from typing import List, Tuple


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        l, r = 0, len(intervals)-1
        while l <= r:
            m = l + (r - l) // 2
            if intervals[m][0] < newInterval[0]:
                l = m + 1
            else:
                r = m - 1
        intervals.insert(l, newInterval)

        rs = []
        for intv in intervals:
            if not rs or rs[-1][1] < intv[0]:
                rs.append(intv)
            else:
                rs[-1][1] = max(rs[-1][1], intv[1])
        return rs
        

class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l : l[0])
        rs = [intervals[0]]
        for intv in intervals:
            if rs[-1][1] < intv[0]:
                rs.append(intv)
                continue
            rs[-1][1] = max(rs[-1][1], intv[1])
        return rs


class OverlapIntervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rs = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
                continue
            rs += 1
            prevEnd = min(prevEnd, end)

        return rs


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class MinMeetingRooms:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line: List[Tuple] = []
        for intv in intervals:
            line.append((intv.start, True))
            line.append((intv.end, False))
        line.sort()

        rs = 0
        cur = 0
        for _, start in line:
            if start:
                cur += 1
                rs = max(rs, cur)
            else:
                cur -= 1
        return rs

