class LengthOfLongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ml = 0
        cset = set()
        while r < len(s):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            ml = max(ml, len(cset))
            r += 1
        return ml

