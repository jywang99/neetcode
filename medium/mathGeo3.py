from typing import List


class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class SpiralOrder:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix), 0, len(matrix[0])

        rs = []
        while up < down and left < right:
            for i in range(left, right):
                rs.append(matrix[up][i])
            up += 1

            for i in range(up, down):
                rs.append(matrix[i][right-1])
            right -= 1

            if not (up < down and left < right):
                break

            for i in range(right-1, left-1, -1):
                rs.append(matrix[down-1][i])
            down -= 1

            for i in range(down-1, up-1, -1):
                rs.append(matrix[i][left])
            left += 1

        return rs


class SetMatrixZeros:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rs, cs = set(), set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rs.add(r)
                    cs.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in rs or c in cs:
                    matrix[r][c] = 0

