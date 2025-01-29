from typing import List


class EvalRPN:
    def is_integer(self, s: str):
        try:
            int(s)
            return True
        except ValueError:
            return False


    def evalRPN(self, tokens: List[str]) -> int:
        ns = []

        for t in tokens:
            if self.is_integer(t):
                ns.append(int(t))
                continue

            x, y = ns.pop(), ns.pop()
            match t:
                case "+":
                    ns.append(x + y)
                case "-":
                    ns.append(y - x)
                case "*":
                    ns.append(x * y)
                case "/":
                    ns.append(int(y / x))
                case _:
                    raise Exception("WTF")

        return ns[0]

