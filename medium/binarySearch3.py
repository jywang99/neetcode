from typing import List


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = None
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                row = matrix[m]
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        if not row:
            return False

        l, r = 0, len(row)-1
        while l <= r:
            m = l + (r - l) // 2
            if row[m] == target:
                return True
            if row[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False

