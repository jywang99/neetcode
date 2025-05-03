from typing import List


class SingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        rs = 0
        for n in nums:
            rs ^= n
        return rs


class HammingWeight:
    def hammingWeight(self, n: int) -> int:
        rs = 0
        for i in range(32):
            if (1 << i) & n:
                rs += 1
        return rs


class CountBits:
    def countBits(self, n: int) -> List[int]:
        rs = []
        for v in range(n+1):
            r = 0
            for i in range(32):
                if (1 << i) & v:
                    r  += 1
            rs.append(r)
        return rs

    def countBitsDP(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n+1):
            dp[i] = dp[i >> 1] + (1 & i)
        return dp


class ReverseBits:
    def reverseBits(self, n: int) -> int:
        rs = 0
        for i in range(32):
            b = (n >> i) & 1
            rs += (b << 31 - i)
        return rs


class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        rs = len(nums)
        for i, n in enumerate(nums):
            rs ^= i ^ n
        return rs

