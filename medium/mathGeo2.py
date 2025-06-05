from typing import List


class SpiralMatrix:
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


class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class SetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zrows, zcols = set(), set()
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zrows.add(r)
                    zcols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zrows or c in zcols:
                    matrix[r][c] = 0


class PowXN:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x: float, n: int) -> float:
            if x == 1 or x == 0:
                return x
            if n == 0:
                return 1

            hf = recurse(x, n // 2)
            rs = hf * hf
            return rs if n % 2 == 0 else rs * x

        rs = recurse(x, abs(n))
        return rs if n >= 0 else 1 / rs


class MultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        digs = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                n1, n2 = int(num1[i]), int(num2[j])
                v = n1 * n2 + digs[i + j]
                digs[i + j] = v % 10
                digs[i + j + 1] += v // 10

        digs.reverse()
        begin = 0
        for i, n in enumerate(digs):
            if n > 0:
                begin = i
                break

        return "".join(map(str, digs[begin:]))

