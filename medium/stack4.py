from typing import List, Tuple


class EvalRPN:
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


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []
        stk = []

        def recurse(opens: int, closes: int):
            if opens == closes == n:
                rs.append("".join(stk))

            if opens < n:
                stk.append("(")
                recurse(opens+1, closes)
                stk.pop()
            if closes < opens:
                stk.append(")")
                recurse(opens, closes+1)
                stk.pop()

        recurse(0, 0)
        return rs


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        rs = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stk:
                if temperatures[stk[-1]] >= t:
                    break
                pi = stk.pop()
                rs[pi] = i - pi
            stk.append(i)

        return rs


class CarFleet:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nears = [i for i in range(len(position))]
        nears.sort(key=lambda i: position[i], reverse=True)
        flts = 0
        lt = 0
        for i in nears:
            time = (target - position[i]) / speed[i]
            if time <= lt:
                continue
            flts += 1
            lt = time
        return flts

