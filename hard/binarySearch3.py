from typing import List


class MedianSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        inf = float("inf")
        n = len(nums1) + len(nums2)
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            ma = (l + r) // 2
            mb = n // 2 - ma - 2

            al = A[ma] if ma >= 0 else -inf 
            bl = B[mb] if mb >= 0 else -inf
            ar = A[ma + 1] if ma + 1 < len(A) else inf
            br = B[mb + 1] if mb + 1 < len(B) else inf

            if al <= br and bl <= ar:
                if n % 2 == 1:
                    return min(ar, br)
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                r = ma - 1
            else:
                l = ma + 1
        
