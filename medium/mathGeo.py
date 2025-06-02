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


class HappyNumber:
    def isHappy(self, n: int) -> bool:
        def nextNum(c: int) -> int:
            rs = 0
            while c:
                rs += (c % 10) ** 2
                c //= 10
            return rs

        s, f = n, n
        while True:
            s = nextNum(s)
            f = nextNum(nextNum(f))
            if f == 1:
                return True
            if s == f:
                return False

