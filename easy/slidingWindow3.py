from typing import List


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mp = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                mp = max(mp, prices[r] - prices[l])
            r += 1
        return mp

