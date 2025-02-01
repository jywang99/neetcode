from typing import List, Tuple


class Solution:
    def str_to_int(self, c: str) -> Tuple[int, bool]:
        try:
            return ( int(c), True )
        except:
            return ( -1, False )

    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            i, ok = self.str_to_int(t)
            if ok:
                stk.append(i)
                continue

            a, b = stk.pop(), stk.pop()
            match t:
                case "+":
                    stk.append(a + b)
                case "-":
                    stk.append(b - a)
                case "*":
                    stk.append(a * b)
                case "/":
                    stk.append(int(b / a))

        return stk[0]


class MinStack:
    def __init__(self):
        self.stk = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.mstk.append(min(self.mstk[-1], val) if self.mstk else val)

    def pop(self) -> None:
        self.stk.pop()
        self.mstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mstk[-1]

