from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: Optional[str] = None

    def add_word(self, word: str) -> None:
        n = self
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.word = word


class WordSearch2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(board), len(board[0])

        rs = []
        root = TrieNode()
        for word in words:
            root.add_word(word)

        visit = set()
        def recurse(r: int, c: int, tn: TrieNode) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in tn.children or (r, c) in visit:
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

