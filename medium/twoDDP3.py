from typing import List


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def recurse(i: int, buy: bool) -> int:
            if i >= len(prices):
                return 0
            k = (i, buy)
            if k in cache:
                return cache[k]

            rs = recurse(i+1, buy)
            if buy:
                rs = max(rs, recurse(i+1, False) - prices[i])
            else:
                rs = max(rs, recurse(i+2, True) + prices[i])

            cache[k] = rs
            return rs

        return recurse(0, True)

