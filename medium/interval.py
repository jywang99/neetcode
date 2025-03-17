from typing import List


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
        
