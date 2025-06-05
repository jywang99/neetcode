from collections import defaultdict
from typing import List


class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                rs.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                rs.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right-1, left-1, -1):
                rs.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                rs.append(matrix[i][left])
            left += 1

        return rs


class SetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zrows, zcols = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zrows.add(r)
                    zcols.add(c)

        for r in zrows:
            for c in range(cols):
                matrix[r][c] = 0

        for c in zcols:
            for r in range(rows):
                matrix[r][c] = 0


class PowXN:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x: float, n: int) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1

            rs = recurse(x, n // 2)
            rs = rs * rs
            return rs if n % 2 == 0 else x * rs

        rs = recurse(x, abs(n))
        return rs if n >= 0 else 1/rs


class MultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        digits = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                v = int(num1[i1]) * int(num2[i2]) + digits[i1 + i2]
                digits[i1 + i2] = v % 10
                digits[i1 + i2 + 1] += v // 10 

        rs = ""
        begin = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 0:
                begin = True
            if begin:
                rs += str(digits[i])
        return rs


class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        tp = tuple(point)
        self.cnt[tp] += 1
        self.pts.append(tp)

    def count(self, point: List[int]) -> int:
        rs = 0
        px, py = point
        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or px == x and py == y:
                continue
            rs += self.cnt[(x, py)] * self.cnt[(px, y)]
        return rs

