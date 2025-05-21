from collections import defaultdict, deque
from typing import Counter, List


class MinWindow:
    def minWindow(self, s: str, t: str) -> str:
        tcnt = Counter(t)
        scnt = defaultdict(int)

        l = 0
        ok = 0
        rs = ""
        rlen = float("inf")
        for r, rc in enumerate(s):
            if rc in tcnt:
                scnt[rc] += 1
                if tcnt[rc] == scnt[rc]:
                    ok += 1

            while ok == len(tcnt):
                nl = r - l + 1
                if nl < rlen:
                    rs = s[l:r+1]
                    rlen = nl

                lc = s[l]
                if lc in tcnt:
                    if scnt[lc] == tcnt[lc]:
                        ok -= 1
                    scnt[lc] -= 1
                l += 1

        return rs


class MaxSlidingWindow:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rs = []
        l = 0
        q = deque()
        for r, nr in enumerate(nums):
            while q and nums[q[-1]] < nr:
                q.pop()
            q.append(r)

            if r + 1 >= k:
                rs.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1

        return rs

