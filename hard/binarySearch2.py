from typing import List


class MedianSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        inf = float("inf")
        n = len(nums1) + len(nums2)
        hf = n // 2
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            am = (l + r) // 2
            bm = hf - am - 2

            al = A[am] if am >= 0 else -inf
            bl = B[bm] if bm >= 0 else -inf
            ar = A[am + 1] if am + 1 < len(A) else inf
            br = B[bm + 1] if bm + 1 < len(B) else inf

            if al <= br and bl <= ar:
                if n % 2 == 1:
                    return min(ar, br)
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                r = am - 1
            else:
                l = am + 1

