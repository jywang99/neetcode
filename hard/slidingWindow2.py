from collections import defaultdict, deque
from typing import Counter, List

class MinWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:
        tcnt = Counter(t)
        scnt = defaultdict(int)

        rs = ""
        ml = float("inf")
        l = ok = 0
        for r in range(len(s)):
            rc = s[r]
            if rc in tcnt:
                scnt[rc] += 1
                if tcnt[rc] == scnt[rc]:
                    ok += 1

            while ok == len(tcnt):
                nl = r - l + 1
                if nl < ml:
                    rs = s[l:r + 1]
                    ml = nl
                
                lc = s[l]
                if lc in tcnt:
                    if scnt[lc] == tcnt[lc]:
                        ok -= 1
                    scnt[lc] -= 1
                l += 1

        return rs


class MaxSlidingWindow:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        rs = []
        l = 0
        for r, nr in enumerate(nums):
            while q and nums[q[-1]] < nr:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                rs.append(nums[q[0]])
                l += 1
        return rs

