from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: Optional[str] = None

    def add_word(self, word: str) -> None:
        n = self
        for c in word:
            nn = None
            if c in n.children:
                nn = n.children[c]
            else:
                nn = TrieNode()
                n.children[c] = nn
            n = nn
        n.word = word


class WordSearch2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        root = TrieNode()
        for word in words:
            root.add_word(word)

        rs, visit = set(), set()
        def recurse(r: int, c: int, tn: TrieNode) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in tn.children or (r, c) in visit:
                return

            ch = board[r][c]
            nn = tn.children[ch]
            if nn.word:
                rs.add(nn.word)
                nn.word = None

            visit.add((r, c))
            for dr, dc in dirs:
                recurse(r+dr, c+dc, nn)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                recurse(r, c, root)

        return list(rs)

