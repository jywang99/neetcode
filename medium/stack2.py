from typing import List


class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.mins.append(min(self.mins[-1], val) if self.mins else val)
        

    def pop(self) -> None:
        self.stk = self.stk[:-1]
        self.mins = self.mins[:-1]
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


class EvalRPN:
    def evalRPN(self, tokens: List[str]) -> int:
        ns: list[int] = []
        for t in tokens:
            match t:
                case "+":
                    ns.append(ns.pop() + ns.pop())
                case "-":
                    y, x = ns.pop(), ns.pop()
                    ns.append(x - y)
                case "*":
                    ns.append(ns.pop() * ns.pop())
                case "/":
                    y, x = ns.pop(), ns.pop()
                    ns.append(int(x / y))
                case _:
                    ns.append(int(t))
        return ns[0]

