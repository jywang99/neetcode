from collections import defaultdict
from typing import Counter


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
        
