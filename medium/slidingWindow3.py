class LongestNoRepeat:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs = 0
        cset = set()
        l = 0
        for c in s:
            while c in cset:
                cset.remove(s[l])
                l += 1
            cset.add(c)
            rs = max(rs, len(cset))
        return rs

