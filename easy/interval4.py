from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class MeetingRooms:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i, intv in enumerate(intervals[1:]):
            pinv = intervals[i]
            if pinv.end > intv.start:
                return False
        return True

