from collections import defaultdict
from typing import Counter


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

