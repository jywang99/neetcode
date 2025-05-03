class GetSum:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        rs, cb = 0, 0
        for i in range(32):
            ab, bb = (a >> i) & 1, (b >> i) & 1
            rs |= (ab ^ bb ^ cb) << i
            cb = (ab & bb) | (bb & cb) | (ab & cb)

        return rs if rs < max_int else ~(rs ^ mask)

