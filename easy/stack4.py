class ValidParen:
    PAIRS = { "{": "}", "(": ")", "[": "]" }

    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in self.PAIRS.keys():
                stk.append(c)
                continue

            if not stk:
                return False

            if self.PAIRS[stk.pop()] != c:
                return False

        return not stk

