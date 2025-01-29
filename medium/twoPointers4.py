from typing import List


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        ml = 0
        ns = set(nums)

        for n in ns:
            if (n-1) in ns:
                continue
            l = 1
            while (n+l) in ns:
                l += 1
            ml = max(l, ml)
            
        return ml
        

class IsPalindrome:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l+1, r-1

        return True


class TwoSum:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            if s < target:
                l += 1
            else:
                r -= 1
        raise Exception("WTF")


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rs = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            if n > 0:
                break

            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    rs.append([ nums[i], nums[l], nums[r] ])
                    l += 1
                    r -= 1
                    while l < r and  nums[l] == nums[l-1]:
                        l += 1

        return rs

