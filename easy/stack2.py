class IsValid:
    PAIRS = { "(": ")", "{": "}", "[": "]" }
    OPENS = PAIRS.keys()


    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False

        stk = []
        for c in s:
            if c in self.OPENS:
                stk.append(c)
                continue
            if not stk: return False
            o = stk.pop()
            if self.PAIRS[o] != c:
                return False
        return len(stk) == 0
        
