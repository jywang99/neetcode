from typing import List


class NQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos, neg = set(), set(), set()
        rs = []
        board = [["."] * n for _ in range(n)]

        def recurse(r: int) -> None:
            if r >= n:
                rs.append(["".join(row) for row in board])
                return

            for c in range(n):
                po = c + r
                ne = c - r
                if c in cols or po in pos or ne in neg:
                    continue

                cols.add(c)
                pos.add(po)
                neg.add(ne)
                board[r][c] = "Q"

                recurse(r + 1)

                cols.remove(c)
                pos.remove(po)
                neg.remove(ne)
                board[r][c] = "."

        recurse(0)
        return rs

