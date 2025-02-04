class LongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        l = 0
        cset = set()
        for r in range(len(s)):
            c = s[r]
            while c in cset:
                cset.remove(s[l])
                l += 1
            cset.add(c)
            ml = max(ml, r - l + 1)
        return ml

