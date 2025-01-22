from typing import List


class IsPalindrome:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
        

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
        
