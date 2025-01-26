class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.mins.append(min(val, self.mins[-1]) if self.mins else val)


    def pop(self) -> None:
        self.mins = self.mins[:-1]
        return self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]

