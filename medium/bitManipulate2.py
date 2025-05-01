from typing import List


class HammingWeight:
    def hammingWeight(self, n: int) -> int:
        rs = 0
        for i in range(32):
            if (1 << i) & n:
                rs += 1
        return rs
        

class SingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        rs = 0
        for n in nums:
            rs ^= n
        return rs

