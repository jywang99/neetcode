class HappyNumber:
    def isHappy(self, n: int) -> bool:
        def getNext(n: int) -> int:
            rs = 0
            while n:
                rs += (n % 10) ** 2
                n //= 10
            return rs

        s, f = n, getNext(n)
        while s != f:
            if f == 1:
                return True
            s = getNext(s)
            f = getNext(getNext(f))

        return s == 1

