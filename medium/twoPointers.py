from typing import List


class TwoSum:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            rs = numbers[l] + numbers[r]
            if rs == target:
                return [ l+1, r+1 ]
            if rs > target:
                r -= 1
            else:
                l += 1

        raise Exception("WTF")
        

class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rs: List[List[int]] = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    rs.append([ nums[i], nums[l], nums[r] ])
                    l, r = l+1, r-1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

        return rs


class MaxArea:
    def maxArea(self, height: List[int]) -> int:
        marea = 0

        l, r = 0, len(height)-1
        while l < r:
            hl, hr = height[l], height[r]
            a = min(hl, hr) * (r - l)
            marea = max(marea, a)
            if hl < hr:
                l += 1
            else:
                r -= 1
    
        return marea

