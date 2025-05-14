from collections import defaultdict, deque
from typing import Counter, List


class MinWindow:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        sc = defaultdict(int)

        rs = ""
        ml = float("inf")

        need = len(tc)
        ok = 0
        l = 0
        for r in range(len(s)):
            rc = s[r]
            if rc in tc:
                sc[rc] += 1
                if sc[rc] == tc[rc]:
                    ok += 1

            while ok == need:
                tl = r - l + 1 
                if tl < ml:
                    ml = tl
                    rs = s[l:r+1]
                lc = s[l]
                if lc in tc:
                    sc[lc] -= 1
                    if sc[lc] < tc[lc]:
                        ok -= 1
                l += 1
        
        return rs
        

class MaxSlidingWindow:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rs = []
        q = deque()
        
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                rs.append(nums[q[0]])
                l += 1

        return rs
        
