class LongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        l = 0
        cset = set()
        for c in s:
            while c in cset:
                cset.remove(s[l])
                l += 1
            cset.add(c)
            ml = max(ml, len(cset))
        return ml

