from typing import List


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recMtx(s: int, t: int) -> int:
            if s > t:
                return -1

            m = (s + t) // 2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                return m
            if matrix[m][0] > target:
                return recMtx(s, m-1)
            return recMtx(m+1, t)

        row = matrix[recMtx(0, len(matrix)-1)]

        def recRow(s: int, t: int) -> int:
            if s > t:
                return -1

            m = (s + t) // 2
            if row[m] == target:
                return m
            if row[m] > target:
                return recRow(s, m-1)
            return recRow(m+1, t)

        return recRow(0, len(row)-1) != -1

