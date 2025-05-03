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


class CountBits:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


class ReverseBits:
    def reverseBits(self, n: int) -> int:
        rs = 0
        i = 0
        while n > 0:
            rs += (n & 1) << (31 - i)
            n >>= 1
            i += 1
        return rs


class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        rs = 0
        for i, num in enumerate(nums):
            rs ^= (i+1) ^ num
        return rs

