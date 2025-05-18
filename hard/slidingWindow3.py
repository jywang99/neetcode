from collections import defaultdict, deque
from typing import Counter, List


class MinWindow:
    def minWindow(self, s: str, t: str) -> str:
        tcnt = Counter(t)
        rs = ""
        mlen = float("inf")

        l = 0
        matches = 0
        scnt = defaultdict(int)
        for r, rc in enumerate(s):
            if rc in tcnt:
                scnt[rc] += 1
                if scnt[rc] == tcnt[rc]:
                    matches += 1

            while matches == len(tcnt):
                ml = r - l + 1
                if ml < mlen:
                    mlen = ml
                    rs = s[l:r+1]
                
                lc = s[l]
                if lc in tcnt:
                    if scnt[lc] == tcnt[lc]:
                        matches -= 1
                    scnt[lc] -= 1
                l += 1

        return rs
        

class MaxSlidingWindow:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rs = []
        q = deque()
        l = 0
        for r in range(len(nums)):
            rv = nums[r]
            while q and nums[q[-1]] < rv:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                rs.append(nums[q[0]])
                l += 1

        return rs

