from typing import List


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                mp = max(mp, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return mp

