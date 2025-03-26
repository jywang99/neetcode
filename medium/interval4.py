from typing import List


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)-1
        while l <= r:
            m = l + (r - l) // 2
            if intervals[m][0] > newInterval[0]:
                r = m - 1
            else:
                l = m + 1

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
        intervals.sort()
        rs = []
        for intv in intervals:
            if not rs or rs[-1][1] < intv[0]:
                rs.append(intv)
            else:
                rs[-1][1] = max(rs[-1][1], intv[1])
        return rs


class EraseOverlapIntervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        rs = 0
        for intv in intervals[1:]:
            if prevEnd > intv[0]:
                prevEnd = min(prevEnd, intv[1])
                rs += 1
            else:
                prevEnd = intv[1]
        return rs


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class MeetingRooms2:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line = []
        for intv in intervals:
            line.append((intv.start, True))
            line.append((intv.end, False))
        line.sort()

        cur, rs = 0, 0
        for p in line:
            if p[1]:
                cur += 1
                rs = max(rs, cur)
            else:
                cur -= 1
        return rs

