from collections import defaultdict
from typing import Counter

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

