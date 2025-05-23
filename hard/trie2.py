from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: str|None = None

    def add_word(self, word: str) -> None:
        n = self
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.word = word


class WordSearch2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        rows, cols = len(board), len(board[0])

        visit, rs = set(), []
        def recurse(r: int, c: int, tn: TrieNode) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in visit or board[r][c] not in tn.children:
                return

            ch = board[r][c]
            nn = tn.children[ch]
            if nn.word:
                rs.append(nn.word)
                nn.word = None

            visit.add((r, c))
            for dr, dc in dirs:
                recurse(r+dr, c+dc, nn)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                recurse(r, c, root)

        return rs

