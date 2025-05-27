from typing import List


class NQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos, neg = set(), set(), set()
        rs = []

        board = [["."] * n for _ in range(n)]
        def recurse(r: int):
            if r >= n:
                rs.append(["".join(row) for row in board])
                return

            for c in range(n):
                po = r - c
                ne = r + c
                if c in cols or po in pos or ne in neg:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                pos.add(po)
                neg.add(ne)

                recurse(r+1)

                board[r][c] = "."
                cols.remove(c)
                pos.remove(po)
                neg.remove(ne)

        recurse(0)
        return rs
        

print(NQueens().solveNQueens(4))

