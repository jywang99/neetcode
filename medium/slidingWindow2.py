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


class CheckInclusion:
    def sameCharCount(self, s1c, s2c):
        for i in range(26):
            if s1c[i] != s2c[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1c, s2c = [0]*26, [0]*26
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord("a")] += 1
            s2c[ord(s2[i]) - ord("a")] += 1

        l, r = 0, len(s1)-1
        while r < len(s2)-1:
            if self.sameCharCount(s1c, s2c):
                return True

            s2c[ord(s2[l]) - ord("a")] -= 1
            l += 1

            r += 1
            s2c[ord(s2[r]) - ord("a")] += 1

        return self.sameCharCount(s1c, s2c)

