from typing import List


class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def recurse(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = recurse(i+1) + recurse(i+2)
            return cache[i]
        
        return recurse(0)


class CostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def recurse(i: int) -> int:
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return cache[i]

        return min(recurse(0), recurse(1))
        
